"""Build local movie recommender artifacts from the TMDB 5000 CSV files.

Keep generated pickle files local; the dense similarity matrix is large and should
not be committed to Git.
"""
import ast
import pickle
import re
from pathlib import Path

import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
MOVIES_CSV = BASE_DIR / "tmdb_5000_movies.csv"
CREDITS_CSV = BASE_DIR / "tmdb_5000_credits.csv"
OUTPUT_DIR = BASE_DIR / "model"


def parse_records(value):
    """Parse a CSV JSON-like list safely; return an empty list for missing values."""
    if not isinstance(value, str) or not value.strip():
        return []
    try:
        result = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return []
    return result if isinstance(result, list) else []


def names(value, limit=None, director_only=False):
    records = parse_records(value)
    if director_only:
        records = [item for item in records if item.get("job") == "Director"][:1]
    elif limit is not None:
        records = records[:limit]
    return [
        re.sub(r"\s+", "", str(item.get("name", "")))
        for item in records
        if isinstance(item, dict) and item.get("name")
    ]


def list_names(value):
    return [
        re.sub(r"\s+", "", str(item.get("name", "")))
        for item in parse_records(value)
        if isinstance(item, dict) and item.get("name")
    ]


def main():
    if not MOVIES_CSV.is_file() or not CREDITS_CSV.is_file():
        raise FileNotFoundError(
            "Place tmdb_5000_movies.csv and tmdb_5000_credits.csv beside "
            "build_artifacts.py. Download the TMDB 5000 Movie Metadata dataset first."
        )

    movies = pd.read_csv(MOVIES_CSV)
    credits = pd.read_csv(CREDITS_CSV)
    required_movies = {"title", "overview", "genres", "keywords"}
    required_credits = {"title", "movie_id", "cast", "crew"}
    if missing := required_movies - set(movies.columns):
        raise ValueError(f"Movies CSV is missing columns: {sorted(missing)}")
    if missing := required_credits - set(credits.columns):
        raise ValueError(f"Credits CSV is missing columns: {sorted(missing)}")

    merged = movies.merge(credits, on="title", how="inner", validate="many_to_many")
    merged = merged.dropna(subset=["title"]).copy()
    merged["overview"] = merged["overview"].fillna("").map(
        lambda value: str(value).split()
    )
    merged["genres"] = merged["genres"].map(list_names)
    merged["keywords"] = merged["keywords"].map(list_names)
    merged["cast"] = merged["cast"].map(lambda value: names(value, limit=3))
    merged["crew"] = merged["crew"].map(
        lambda value: names(value, director_only=True)
    )

    merged["tags"] = (
        merged["overview"]
        + merged["genres"]
        + merged["keywords"]
        + merged["cast"]
        + merged["crew"]
    )
    movie_list = merged[["title", "movie_id", "tags"]].copy()
    movie_list["tags"] = movie_list["tags"].map(
        lambda values: " ".join(values).lower()
    )

    stemmer = PorterStemmer()

    def stem(text):
        return " ".join(stemmer.stem(token) for token in text.split())

    movie_list["tags"] = movie_list["tags"].map(stem)
    vectorizer = CountVectorizer(max_features=5000, stop_words="english")
    vectors = vectorizer.fit_transform(movie_list["tags"])
    similarity = cosine_similarity(vectors)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    export_list = movie_list[["title", "movie_id"]].reset_index(drop=True)
    with (OUTPUT_DIR / "movie_list.pkl").open("wb") as file:
        pickle.dump(export_list, file, protocol=pickle.HIGHEST_PROTOCOL)
    with (OUTPUT_DIR / "similarity.pkl").open("wb") as file:
        pickle.dump(similarity, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Exported {len(export_list):,} movies to {OUTPUT_DIR}")
    print(f"Similarity matrix shape: {similarity.shape}")


if __name__ == "__main__":
    main()

import os
import pickle
from pathlib import Path

import requests
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def fetch_poster(movie_id):
    """Return a TMDB poster URL when configured; otherwise omit the poster."""
    if not TMDB_API_KEY:
        return None
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={"api_key": TMDB_API_KEY, "language": "en-US"},
            timeout=10,
        )
        response.raise_for_status()
        poster_path = response.json().get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except (requests.RequestException, ValueError):
        pass
    return None


def recommend(movie):
    matches = movies.index[movies["title"] == movie]
    if len(matches) == 0:
        return []
    index = matches[0]
    distances = sorted(
        enumerate(similarity[index]), key=lambda item: item[1], reverse=True
    )
    recommendations = []
    for movie_index, score in distances:
        if movie_index == index:
            continue
        row = movies.iloc[movie_index]
        recommendations.append(
            {"title": row["title"], "poster": fetch_poster(row["movie_id"])}
        )
        if len(recommendations) == 5:
            break
    return recommendations


st.set_page_config(page_title="Movie Recommender System", page_icon="🎬")
st.title("Movie Recommender System")

movie_list_path = MODEL_DIR / "movie_list.pkl"
similarity_path = MODEL_DIR / "similarity.pkl"
if not movie_list_path.is_file() or not similarity_path.is_file():
    st.error(
        "Model artifacts are missing. Export movie_list.pkl and similarity.pkl "
        "from the notebook into the Movie-Recommender_system/model/ folder, "
        "then restart the app."
    )
    st.stop()

try:
    with movie_list_path.open("rb") as file:
        movies = pickle.load(file)
    with similarity_path.open("rb") as file:
        similarity = pickle.load(file)
except (OSError, pickle.UnpicklingError, EOFError) as exc:
    st.error(f"Could not load recommender artifacts: {exc}")
    st.stop()

if movies.empty or "title" not in movies.columns or "movie_id" not in movies.columns:
    st.error("The movie-list artifact is empty or missing required columns.")
    st.stop()

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movies["title"].dropna().tolist()
)

if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)
    if not recommendations:
        st.warning("No recommendations could be generated for this title.")
    else:
        columns = st.columns(len(recommendations))
        for column, item in zip(columns, recommendations):
            with column:
                st.write(item["title"])
                if item["poster"]:
                    st.image(item["poster"], use_container_width=True)
        if not TMDB_API_KEY:
            st.caption(
                "Posters are optional. Set TMDB_API_KEY to enable poster images."
            )

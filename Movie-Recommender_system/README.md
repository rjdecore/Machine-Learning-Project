# Movie Recommendation System — Python + Streamlit

## Objective
Build a content-based recommendation system that returns movies similar to a selected title using movie metadata.

## How it works
1. Combine overview, genres, keywords, selected cast and director into a text feature.
2. Normalize the text and create a bag-of-words representation with CountVectorizer.
3. Calculate cosine similarity between movie vectors.
4. Return five similar titles from the saved similarity matrix.

This is a content-similarity baseline. It does not learn personal preferences from user ratings, and recommendation quality still needs evaluation.

## Dataset sources

**Dataset required by this project:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). Download `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`, then place both files in this folder beside `build_artifacts.py`.

**IMDb dataset reference:** [IMDb non-commercial datasets](https://datasets.imdbws.com/). These are official IMDb TSV files and are a separate data source. They are **not drop-in replacements** for the two TMDB CSVs expected by the current builder; using IMDb data would require a different preprocessing/feature pipeline and attention to IMDb's dataset terms.

## Run locally

From this directory:

```bash
pip install -r requirements.txt
python build_artifacts.py
streamlit run app.py
```

The builder creates `model/movie_list.pkl` and `model/similarity.pkl` with aligned row order. Generated pickle files are intentionally ignored by Git because the dense similarity matrix is large. Do not load pickle artifacts from untrusted sources.

## Posters (optional)
The Streamlit app can use the TMDB API to fetch posters. Set the `TMDB_API_KEY` environment variable locally if you want posters. Do not commit API keys. Recommendations can still be shown without posters.

## Business question and value
**Question:** Given a selected title, which five movies have the most similar metadata in this dataset?

**Business use:** Similar-item recommendations can help viewers discover related titles. The current result is based on metadata similarity, not a measured lift in watch time or satisfaction. To assess quality, create a held-out evaluation or collect user feedback.

## Reproducibility and limitations
- The source CSVs and generated artifacts are not stored in this repository; download the dataset and build the artifacts locally.
- The builder checks for required files/columns and reports a clear error if the data is missing.
- The full-data inference path has not been claimed as end-to-end verified until the CSVs are available and the generated artifacts have been tested locally.

## Project files
- `build_artifacts.py` — preprocessing and model-artifact builder
- `app.py` — Streamlit application
- `Movie_recommender_system.ipynb` — main notebook
- `notebook86c26b4f17.ipynb` — supporting notebook
- [Code PDF](code.pdf)

## Tech stack
Python, Pandas, scikit-learn, NLTK, cosine similarity, Streamlit, optional TMDB API.

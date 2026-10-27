# Movie Recommendation System — Python + Streamlit

## Objective
Build a content-based recommendation system that returns similar movies based on movie metadata.

## Method
- Content-based filtering
- Feature similarity
- Cosine similarity
- Persisted recommendation data/model artifacts

## Application
The Streamlit app lets a user select a movie and returns **5 similar recommendations** with posters and titles.

## Run locally

From this project directory, install the app dependencies and run `streamlit run app.py`:

```bash
pip install -r requirements.txt
python build_artifacts.py
streamlit run app.py
```

**Reproducibility note:** the repository does not include the TMDB 5000 CSVs or generated model artifacts. Download `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` from the [TMDB Movie Metadata dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place them beside `build_artifacts.py`. Generate artifacts with `python build_artifacts.py`; it creates `model/movie_list.pkl` and `model/similarity.pkl` with aligned row order. The dense similarity matrix is large, so generated pickle files are intentionally ignored by Git rather than committed. The notebook's final export cells were also corrected.

## External Integration
TMDB API is optional and is used only to retrieve movie posters. To enable posters, set the `TMDB_API_KEY` environment variable; the key is no longer embedded in source code. Without a key, movie recommendations can still be displayed without posters.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | Cosine Similarity | Streamlit | TMDB API**

## Business Questions & Value
**Question:** Given a selected movie, which five titles are most similar according to the project's metadata-based similarity method?

**Finding to communicate:** The app returns five recommendations based on cosine similarity. This demonstrates content similarity, not necessarily user preference or recommendation relevance; quality would need a user-rating or offline ranking evaluation.

**Business use:** Content platforms can use similar-item recommendations to improve discovery and keep users exploring related titles.

## Report / PDF
[Open the project code PDF](code.pdf), notebook and Streamlit app.

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

## External Integration
TMDB API is used to retrieve movie posters for the recommended titles.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | Cosine Similarity | Streamlit | TMDB API**

## Business Questions & Value
**Question:** Given a selected movie, which five titles are most similar according to the project's metadata-based similarity method?

**Finding to communicate:** The app returns five recommendations based on cosine similarity. This demonstrates content similarity, not necessarily user preference or recommendation relevance; quality would need a user-rating or offline ranking evaluation.

**Business use:** Content platforms can use similar-item recommendations to improve discovery and keep users exploring related titles.

## Report / PDF
The Streamlit app and notebook/code artifacts are the primary demonstration; no project-specific PDF was identified in the folder listing.

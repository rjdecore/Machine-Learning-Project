# Movie Recommendation System

This project implements a content-based movie recommendation system using Python and the Pandas, Numpy, NLTK, and Scikit-learn libraries. The system recommends movies similar to a given movie based on their genres, keywords, cast, and crew.


## Dataset
Downlod From Kaggle
The system uses the TMDB 5000 Movie Dataset, which contains information about 5000 movies, including their title, overview, genres, keywords, cast, and crew.


## Methodology

1. Data Loading and Cleaning: The dataset is loaded into a Pandas DataFrame, and missing values and duplicates are removed.
2. Feature Engineering: New features are created from the existing features, such as a "tags" feature that combines the movie's overview, genres, keywords, cast, and crew.
3. Text Preprocessing: The "tags" feature is preprocessed using stemming and stop word removal.
4. Text Vectorization: The preprocessed "tags" feature is vectorized using the CountVectorizer class from Scikit-learn.
5. Cosine Similarity: The cosine similarity between the vectors of all movies is calculated to determine the similarity between them.
6. Recommendation Generation: When a user inputs a movie title, the system finds the movies with the highest cosine similarity scores to the given movie and recommends them to the user.


## Usage

1. Install the required libraries:

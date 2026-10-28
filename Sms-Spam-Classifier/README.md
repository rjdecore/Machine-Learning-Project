# SMS Spam Detection — Machine Learning + Streamlit

## Objective
Classify incoming SMS messages as **Spam** or **Not Spam (Ham)**.

## NLP Workflow
**Text preprocessing → TF-IDF vectorization → Multinomial Naive Bayes → prediction → Streamlit UI**

## Text Preparation
The project applies text-cleaning steps including tokenization, stopword handling, punctuation removal, and stemming before vectorization.

## Model
**Multinomial Naive Bayes** trained on TF-IDF features.

## Application
The Streamlit interface accepts a message and returns its predicted class.

## Tech Stack
**Python | NLP | TF-IDF | Multinomial Naive Bayes | Scikit-learn | Streamlit**
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

## Business Questions & Value
**Question:** Does the text classifier label an incoming SMS as spam or ham using the trained TF-IDF and Multinomial Naive Bayes pipeline?

**Finding to communicate:** The app returns a predicted class for the entered message. Include precision, recall, F1 and a confusion matrix from held-out data before claiming how reliably spam is detected.

**Business use:** This illustrates a message-filtering workflow. False positives can hide legitimate messages, so any real deployment needs threshold review and monitoring.

## Report / PDF
Use the notebook, dataset and Streamlit app as the primary artifacts; no project-specific PDF was identified in the folder listing.

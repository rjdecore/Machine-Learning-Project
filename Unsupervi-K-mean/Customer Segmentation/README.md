# Customer Segmentation — K-Means Clustering

## Objective
Segment customers into meaningful groups using demographic and behavioral attributes.

## Data Preparation
- Median imputation for numeric fields
- Mode imputation for categorical fields
- One-hot encoding
- StandardScaler
- Train/test feature alignment

## Clustering
- K-Means clustering
- Elbow method for selecting cluster count
- Cluster assignment for training data
- Cluster prediction for new/test data

## Application
A Streamlit interface accepts customer attributes and predicts the corresponding cluster using the saved preprocessing and clustering model.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | K-Means | StandardScaler | Streamlit**
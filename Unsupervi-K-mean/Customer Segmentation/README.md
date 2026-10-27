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

## Business Questions & Value
**Question:** Which cluster does a customer most closely resemble based on the selected demographic and behavioral attributes?

**Finding to communicate:** The app assigns a cluster using the saved preprocessing and K-Means model. Describe cluster profiles using the feature summaries in the notebook; cluster numbers are labels, not ordered scores or business segments until interpreted.

**Business use:** Teams can use interpretable cluster profiles to design differentiated customer research or campaign hypotheses. Validate segment stability and business usefulness before deploying campaigns.

## Report / PDF
The notebook, data and Streamlit app are the primary artifacts; no project-specific PDF was identified in the listing.

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Page Config
st.set_page_config(page_title="Amazon Music Clustering", layout="wide")

st.title("🎵 Amazon Music Clustering Dashboard")

# Load Dataset
df = pd.read_csv("amazon_music_final_clusters.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Model Comparison
st.subheader("Model Comparison")

comparison_data = {
    "Algorithm": ["KMeans", "DBSCAN","Hierarchical"],
    "Silhouette Score": [0.242307, 0.699230,0.274350],
    "Davies-Bouldin Index": [1.570216, 0.318855,1.487665
]
}

comparison_df = pd.DataFrame(comparison_data)
st.dataframe(comparison_df)

# Final Best Model Section
st.subheader("🏆 Final Best Model")

st.success("""
Final Best Model: DBSCAN

Justification:
 -> Highest Silhouette Score: 0.699230
 -> Lowest Davies-Bouldin Index: 0.318855
 -> Noise Handling: DBSCAN identified 0.75% of songs as outliers.
""")

# DBSCAN Cluster Distribution
st.subheader("DBSCAN Cluster Distribution")

cluster_counts = df['db_cluster'].value_counts()

fig, ax = plt.subplots()
ax.bar(cluster_counts.index.astype(str), cluster_counts.values)
ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Songs")

st.pyplot(fig)

# PCA Visualization
st.subheader("PCA Visualization (DBSCAN Clusters)")

features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo', 'duration_ms'
]

X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)

fig2, ax2 = plt.subplots()
scatter = ax2.scatter(
    pca_data[:, 0],
    pca_data[:, 1],
    c=df['db_cluster'],
    cmap="viridis",
    alpha=0.6
)

ax2.set_xlabel("PCA 1")
ax2.set_ylabel("PCA 2")

st.pyplot(fig2)

# Feature Analysis (Cluster-wise Mean)
st.subheader("Feature Analysis by DBSCAN Cluster")

selected_feature = st.selectbox("Select Audio Feature:", features)

# Calculate mean of selected feature per cluster
cluster_means = df.groupby('db_cluster')[selected_feature].mean()

fig3, ax3 = plt.subplots()
ax3.bar(cluster_means.index.astype(str), cluster_means.values)

ax3.set_xlabel("DBSCAN Cluster")
ax3.set_ylabel(f"Average {selected_feature}")
ax3.set_title(f"Average {selected_feature} per Cluster")

st.pyplot(fig3)

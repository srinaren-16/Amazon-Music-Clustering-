# 🎵 Amazon Music Clustering

## 📌 Project Overview

With millions of songs available on streaming platforms, manually categorizing tracks into genres or moods is impractical.

This project applies **Unsupervised Machine Learning** techniques to automatically group songs based on their audio characteristics such as danceability, energy, tempo, and acousticness.

The objective is to discover meaningful clusters that represent similar musical styles — without using predefined genre labels.

---

## 🎯 Problem Statement

Streaming platforms require intelligent systems to:

- Organize massive song libraries
- Improve song discovery
- Enhance playlist recommendations
- Analyze listening behavior

This project uses clustering algorithms to group songs based purely on audio features.

---

## 🏢 Business Use Cases

### 🎧 Personalized Playlist Curation
Automatically group similar songs to enhance playlist generation.

### 🔍 Improved Song Discovery
Recommend tracks based on audio similarity instead of only genre tags.

### 🎤 Artist & Competitor Analysis
Identify songs that fall into similar audio clusters.

### 📊 Market Segmentation
Analyze listening behavior patterns using cluster groups.

---

## 🛠️ Skills & Concepts Applied

- Data Exploration (EDA)
- Data Cleaning
- Feature Selection
- Feature Scaling (StandardScaler)
- K-Means Clustering
- DBSCAN
- Hierarchical Clustering
- Elbow Method
- Silhouette Score
- Davies-Bouldin Index
- PCA (Dimensionality Reduction)
- Cluster Visualization
- Model Comparison
- Data Storytelling
- Streamlit Deployment

---

## 📂 Dataset Information

**File Name:** `single_genre_artists.csv`

### 🔑 Audio Features Used

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo  
- duration_ms  

These features describe rhythm, mood, intensity, and instrumentation of songs.

---

## 🔄 Project Workflow

### 1️⃣ Data Exploration & Preprocessing

- Loaded dataset using Pandas
- Checked missing values and duplicates
- Removed unnecessary text and ID columns
- Standardized numerical features using `StandardScaler`

---

### 2️⃣ Feature Selection

Selected only relevant audio features for clustering.

---

### 3️⃣ Dimensionality Reduction (PCA)

Used PCA to reduce high-dimensional data into 2D for visualization purposes.

---

### 4️⃣ Clustering Techniques Applied

#### 🔹 K-Means Clustering
- Used Elbow Method to determine optimal k
- Evaluated using Silhouette Score
- Generated 3 clusters

#### 🔹 DBSCAN
- Density-based clustering
- Identified natural groupings
- Detected outliers (~0.75%)

#### 🔹 Hierarchical Clustering
- Used Ward linkage method
- Visualized cluster formation using dendrogram

---

## 📊 Model Comparison

| Algorithm      | Silhouette Score | Davies-Bouldin Index |
|---------------|-----------------|----------------------|
| KMeans        | 0.242307        | 1.570216             |
| DBSCAN        | 0.699230        | 0.318855             |
| Hierarchical  | 0.274350        | 1.487665             |

---

## 🏆 Final Best Model: DBSCAN

**Justification:**

- Highest Silhouette Score: 0.699230  
- Lowest Davies-Bouldin Index: 0.318855  
- Noise Handling: DBSCAN identified 0.75% of songs as outliers  

DBSCAN achieved the strongest mathematical cluster separation among evaluated models.

---

## 📈 Visualizations Included

- Elbow Curve
- PCA 2D Scatter Plot
- DBSCAN Cluster Distribution
- Hierarchical Clustering Dendrogram

---

## 📤 Final Output

Final dataset exported as:
amazon_music_final_clusters.csv

---

## 🖥️ Streamlit Dashboard

Make a Streamlit dashboard to visualize the best model.

---
##  Project Structure

```text
Amazon-Music-Clustering/
│
├── Amazon_music_clustering.ipynb
├── Single Genre Artists.csv
├── amazon_music_final_clusters.csv
├── app.py
├── requirements.txt
├── README.md


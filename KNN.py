import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Streamlit App Title
st.title("K-Means Clustering using Streamlit")

# Upload CSV File
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataset
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Select Features for Clustering
    st.write("### Select Features for Clustering")
    selected_features = st.multiselect("Choose at least 2 features:", df.columns)

    if len(selected_features) >= 2:
        data = df[selected_features]

        # Standardizing the data
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)

        # Select Number of Clusters (K)
        k = st.slider("Select Number of Clusters (K)", 2, 10, 3)

        # Apply K-Means Clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        clusters = kmeans.fit_predict(scaled_data)

        # Add Cluster Labels to DataFrame
        df["Cluster"] = clusters

        # Display Clustered Data
        st.write("### Clustered Data")
        st.dataframe(df)

        # Visualizing Clusters (Only for 2D Data)
        if len(selected_features) == 2:
            st.write("### Cluster Visualization")
            fig, ax = plt.subplots()
            scatter = ax.scatter(
                df[selected_features[0]], df[selected_features[1]], c=clusters, cmap="viridis"
            )
            ax.set_xlabel(selected_features[0])
            ax.set_ylabel(selected_features[1])
            ax.set_title("K-Means Clustering")
            plt.colorbar(scatter, label="Cluster")
            st.pyplot(fig)
        else:
            st.warning("Visualization is only available for 2 selected features.")

    else:
        st.warning("Please select at least 2 features for clustering.")

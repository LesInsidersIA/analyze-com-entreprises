from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def kmeans_clustering(df, n_clusters):
    # Ne garder que les colonnes numériques
    df_clustering = df.select_dtypes(include=['float64', 'int64'])
    print(df_clustering.columns)

    # Normaliser les données
    scaler = StandardScaler()
    df_clustering_scaled = scaler.fit_transform(df_clustering)

    # Effectuer le clustering avec K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(df_clustering_scaled)

    # Ajouter les labels de cluster à la DataFrame d'origine
    df['Cluster'] = kmeans.labels_

    # Afficher les moyennes des variables par cluster
    print(df.groupby('Cluster').mean())

    # Visualiser les clusters
    plt.figure(figsize=(16, 8))
    plt.scatter(df_clustering.iloc[:, 0], df_clustering.iloc[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.title("Clustering des entreprises par secteur d'activités et capital social")
    plt.xlabel(df_clustering.columns[0])
    plt.ylabel(df_clustering.columns[1])
    plt.annotate("Source : Youssouf SAGAF", xy=(df_clustering.iloc[:, 0].max() / 2, df_clustering.iloc[:, 1].max() / 2), 
                fontsize=10, ha="center", rotation=30, alpha=0.3)
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# 1. Load Dataset (Colab upload or Jupyter local file)
#try:
 #   from google.colab import files
  #  df = pd.read_csv(list(files.upload().keys())[0])
#except ImportError:
df = pd.read_csv("customers.csv")

# 2. Select numerical features for clustering [Annual_Income, Spending_Score]
X = df.iloc[:, [3, 4]].values

# 3. Plot Dendrogram to determine optimal number of clusters
plt.figure(figsize=(8, 4))
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Customer Data Points')
plt.ylabel('Euclidean Distances')
plt.show()

# 4. Construct Agglomerative Hierarchical Clustering Model
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

# 5. Display Clustered Output
df['Cluster'] = y_hc
print("--- CLUSTER ASSIGNMENTS ---")
print(df[['CustomerID', 'Annual_Income', 'Spending_Score', 'Cluster']])
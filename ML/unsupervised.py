import numpy as np
import matplotlib.pyplot as plt

# Kmeans is the Algorithm from Scikit-learn
from sklearn.cluster import KMeans

X=np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]]) # 2 Clusters

#cluster 1 - [1,2],[1,4],[1,0]
#cluster 2 - [10,2],[10,4],[10,0]

KMeans = KMeans(n_clusters= 2)

KMeans.fit(X)

plt.scatter(X[:,0], X[:,1],c= KMeans.labels_)

plt.show()








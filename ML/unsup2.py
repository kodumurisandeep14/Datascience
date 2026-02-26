import numpy as np
from sklearn.cluster import DBSCAN

X= np.array ([[1,2],[2,3],[8,8],[9,9],[50,2]])

model = DBSCAN (eps=2,min_samples=2)

labels =model.fit_predict(X)

print(labels)


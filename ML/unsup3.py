import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

X = np.array([[1,2,3],
              [2,3,4],
              [3,4,5],
              [5,6,7]])

pca = PCA(n_components=2)
X_new = pca.fit_transform(X)
plt.scatter(X_new[:,0],X_new[:,1])

plt.show()
print(X_new)
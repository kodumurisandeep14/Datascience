import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X=np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])

y=np.array([0,0,0,1,1,1])

model= KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

new_student = np.array([[1,3]])

pred = model.predict(new_student)

print(pred)
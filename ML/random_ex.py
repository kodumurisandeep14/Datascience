import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

X= np.array([[1,60],
             [2,65],
             [3,70],
             [4,80],
             [5,85],
             [6,90],
             [7,95],
             [8,98]])
y= np.array([0,0,0,1,1,1,1,1])

model = RandomForestClassifier(n_estimators=10)

model.fit(X,y)

prediction = model.predict([[3,75]])

print(prediction)

acc = model.score(X,y)
print(acc)

plt.scatter(X[:,0], X[:,1], c=y)
plt.scatter(3, 75, color='red', s=100)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Random Forest Decision Boundary")
plt.show()
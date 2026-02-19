import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

import matplotlib.pyplot as plt

X=np.array([[25,40000],
   [30,60000],
   [40,80000],
   [20,30000],
   [30,120000]])

y=np.array([0,1,1,0,1])

model=DecisionTreeClassifier()

model.fit(X,y)
pred = model.predict([[35,50000]])

# plt.figure( figsize=(10,6))
# tree.plot_tree(model,filled=True)
# plt.show()


print(pred)

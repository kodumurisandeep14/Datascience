import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #importing linear regression algorithm from scikitlearn library

size = np.array([500,800,1000,1200,1500]).reshape(-1,1)
prices = np.array([100000,150000,200000,250000,300000])

model = LinearRegression();
model.fit(size,prices)

new_size = np.array([[1100]])
predicted_price = model.predict(new_size)
print(predicted_price[0])

plt.scatter(size,prices,color="blue")
plt.plot(size,model.predict(size),color="red")
plt.xlabel("SQFT")
plt.ylabel("COST")
plt.title("First AI Example")
plt.show()

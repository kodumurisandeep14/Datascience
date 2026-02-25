from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #importing linear regression algorithm from scikitlearn library

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials= True,
                   allow_methods=["*"],
                   allow_headers=["*"])

size = np.array([500,800,1000,1200,1500]).reshape(-1,1)
prices = np.array([100000,150000,200000,250000,300000])

model = LinearRegression();
model.fit(size,prices)

@app.get("/predict/{sqft}")
def predict_price(sqft: int):
    new_size=np.array([[sqft]])
    predicted_price = model.predict(new_size)
    return {
        "Size" : sqft,
        "Predicted_price": float(predicted_price[0])
    }






# plt.scatter(size,prices,color="blue")
# plt.plot(size,model.predict(size),color="red")
# plt.xlabel("SQFT")
# plt.ylabel("COST")
# plt.title("First AI Example")
# plt.show()

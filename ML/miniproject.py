import numpy as np#math
import pandas as pd#tabular
import matplotlib.pyplot as plt#graph
import seaborn as sns#rich graph
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression #true or False
from sklearn.preprocessing import LabelEncoder #text to numbers
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report #report 

data ={
    "tenure":[1,5,10,2,8,15,3,12],
    "Monthly_charges" :[50,60,80,45,70,90,55,85],
    "contract_type": ["month-month","one year","two year","month-month","one year","two year","two year","month-month"],
    "churn" :["Yes","no","Yes","no","Yes","no","Yes","no"]
}
df=pd.DataFrame(data)
le=LabelEncoder()
df["contract_type"] = le.fit_transform(df["contract_type"])
df["churn"]= le.fit_transform(df["churn"])

X= df.drop("churn",axis=1)
y=df["churn"]

X_train,X_test,y_train,y_test =train_test_split (X,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

# print("Accuracy",accuracy_score(y_test,y_pred))
# print("Confusion Matrix",confusion_matrix(y_test,y_pred))
# print("Classification Report",classification_report(y_test,y_pred))

# sns.heatmap(confusion_matrix(y_test,y_pred),annot=True)
# plt.title("Confusion Matrix")
# plt.show()

new_customer =np.array([[4,65,0]])
prediction = model.predict(new_customer)

if prediction[0] ==1:
    print("churn")
else:
    print("No")
    












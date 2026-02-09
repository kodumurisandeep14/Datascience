import seaborn as sns
import matplotlib.pyplot as plt    
import pandas as pd
import numpy as np

df = pd.read_excel("Employee.xlsx")

# sns.barplot(
#     x="Age",
#     y="salary",
#     data=df
# )
sns.violinplot(x="Department",y="salary",data=df)
plt.show()
# print(df)



# sns.violinplot(x="Department",y="salary",data=df)
# sns.set_style("darkgrid")
# corr=df[["age","salary"]].corr()
# sns.heatmap(corr,annot=True,cmap="coolwarm")

# data={
#     "age":[22,25,30,35,40,50],
#     "salary":[25000,30000,35000,40000,50000,60000],
#     "Department":["IT", "HR","IT","Finance", "HR", "Finance"]
# }

# sns.violinplot(x="Department",y="salary",data=df)
# sns.boxplot(x="Department",y="salary",data=df)
# sns.histplot(df["salary"],bins=5,kde=True)
# sns.countplot(x="Department",data=df)
# sns.barplot(x="Department",y="salary",data=df)
# plt.title("Employee Data")
# plt.show()

# sns.lineplot(x="age",y="salary",data=df)
# # sns.scatterplot(
# #     x="age",
# #     y="salary",
# #     data=df
# # )
# plt.title("Employee Data")
# plt.show()


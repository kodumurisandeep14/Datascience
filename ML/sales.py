#used to manipulate tabular data (DataFrame)
import pandas as pd 

#Transaction Encoder 
#apriori Algorithm understand only True/False
from mlxtend.preprocessing import TransactionEncoder

#apriori is used to find the frequency
#association_rules used to create rules
from mlxtend.frequent_patterns import apriori , association_rules

#data set
transactions = [
    ['Milk','Bread'],
    ['Milk','Butter'],
    ['Butter','Bread'],
    ['Milk','Bread'],
    ['Milk','Bread','Butter']
]

#convert Data Frame
te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df= pd.DataFrame(te_data,columns=te.columns_)

#print("Dataset:\n", df)

#Apply Apriori
frequent_items = apriori(df, min_support = 0.6, use_colnames = True)
print("\nFrequent Itemsets:\n" ,frequent_items )

rules= association_rules(frequent_items,metric= "confidence", min_threshold= 0.7)

print("\n Association Rules:\n", rules)

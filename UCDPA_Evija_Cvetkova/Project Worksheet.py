# Import CSV file

import pandas as pd
data=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(data.info())

# Cleaning Data Using pandas
missing_value = data.isnull ().sum()
print(missing_value)
new_data = data.drop(['partner' , 'dependants' , 'phoneservice' , 'paperlessbilling'(axis = 1)
print(data.shape,new_data.shape)
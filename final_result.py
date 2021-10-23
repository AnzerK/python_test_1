import pandas as pd
import numpy as np


df = pd.read_csv("sampledata2.csv")

df = df.iloc[: , 1:]

df.rename(columns= {'Customer_Name' : 'Name', 'Customer_Id' : 'Cust_I', 'Open_Date' : 'Open_Dt', 'Last_Consulted_Date' : 'Consul_Dt', 'Vaccination_Id' : 'VAC_ID', 'Is_Active' : 'Flag' }, inplace=True)

country = df['Country'].unique()

for i in country:
    dfx = df[df['Country'] == i]
    dfx.loc[dfx['Dr_Name'].duplicated(), 'Dr_Name']=np.nan
    dfx.to_csv('Table_%s.csv'%i, index = False)



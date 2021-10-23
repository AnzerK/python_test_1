import pandas as pd

df = pd.read_csv("sampledata1.dsv", sep= "|")

df.dropna(how = 'all', axis = 1, inplace=True)

df.to_csv("sampledata2.csv", index = False)

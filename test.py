import pandas as pd


predictionsCsv = pd.read_csv(r"C:\Users\Brandon\Documents\prediction_1-bitcoin_closed_comment_data_all.csv")

names = predictionsCsv["commenter"].unique(); #1674 unique; total comb=1,400,000 >
z=predictionsCsv.groupby("commenter").size()
print(z.head())
n = z[z > 2]

print(predictionsCsv.loc[predictionsCsv['commenter'].isin(z[z > 2].index)])
print(n)



z=predictionsCsv.groupby("commenter").count()
z[z["commenter"] > 2]

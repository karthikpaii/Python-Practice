import pandas as pd

df = pd.read_csv('sample.csv')
df.fillna(method='bfill', inplace=True)
print(df)

df.to_csv('sample.csv', index=False)

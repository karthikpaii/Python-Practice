import pandas as pd
# making dataframe
df = pd.read_csv("products.csv")
# reshape the dataframe using 
df_stacked = df.stack()
print(df_stacked.head(26))


df_unstacked = df_stacked.unstack()
print(df_unstacked)

df_melt = pd.melt(df, id_vars=['product_id'])
print(df_melt)
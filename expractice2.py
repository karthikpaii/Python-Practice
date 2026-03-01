import pandas as pd 
df = pd.DataFrame({ 
"product":["Pen","Book"], 
"Jan":[100,200], 
"Feb":[150,250] 
}) 
print("original")
print(df)
long_df = pd.melt(df, id_vars="product", var_name="Month", value_name="Sales") 
wide_df = long_df.pivot(index="product", columns="Month", values="Sales") 
print(long_df) 
print(wide_df) 
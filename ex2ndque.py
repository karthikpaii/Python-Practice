import pandas as pd

df1 = pd.DataFrame({"emp_id":[1,2,3], "name":["A","B","C"]})
df2 = pd.DataFrame({"emp_id":[2,3,4], "salary":[40000,50000,60000]})

inner = pd.merge(df1, df2, on="emp_id", how="inner")
outer = pd.merge(df1, df2, on="emp_id", how="outer")
left = pd.merge(df1, df2, on="emp_id", how="left")
right = pd.merge(df1, df2, on="emp_id", how="right")

print(inner)
print(outer)
print(left)
print(right)

import pandas as pd

def normalize(df):
    return (df - df.min()) / (df.max() - df.min())

data = pd.DataFrame({"marks":[50,70,90], "age":[15,16,17]})

norm_data = normalize(data)
print(norm_data)


import pandas as pd



df = pd.DataFrame({"marks":[50,70,90], "age":[15,16,17]})

h= (df - df.min()) / (df.max() - df.min())
norm_data = normalize(h)
print(norm_data)

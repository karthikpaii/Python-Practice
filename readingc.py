import pandas as pd

data=pd.read_csv('products.csv')
df=pd.DataFrame(data)
print(df)

df.drop(2,inplace=True,axis=0)
print(df)

new=df.dropna()
print(new)

dup=df.drop_duplicates()
print(dup)

data= { 
'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 'city': ['New York', 'Paris', 'London', 'Tokyo'] 
}
col=['A','B','C','D']
df2=pd.DataFrame(data,index=col)
print(df2)

df2.set_index('name',inplace=True)
print(df2)

df2.reset_index(inplace=True)
print(df2)
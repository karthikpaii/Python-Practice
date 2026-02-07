import pandas as pd

x=[3,4,5,6,7]
var=pd.Series(x)
print(var)

print(type(var))
print(var[2])

y=[3,4,5,6,7]
index=['a','b','c','d','e']
var2=pd.Series(y,index,dtype='float',name='python')
print(var2)

dic={"name":['python','css','c++','java'],"numbers":[1,2,3,4], "rank":[1,2,3,4]}
var3=pd.Series(dic)
print(var3)
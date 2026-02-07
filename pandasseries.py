import pandas as pd

x=[3,4,5,6,7]
var=pd.Series(x)
print(var)

print(type(var))
print(var[2])

#creating series
y=[3,4,5,6,7]
index=['a','b','c','d','e']
var2=pd.Series(y,index,dtype='float',name='python')
print(var2)


#passing dictionary to series
dic={"name":['python','css','c++','java'],"numbers":[1,2,3,4], "rank":[1,2,3,4]}
var3=pd.Series(dic)
print(var3)


#creating series of single data
s=pd.Series(12)
print(s)

#creating series of single data multiple tiimes
s=pd.Series(12,index)
print(s)

#
s1=pd.Series(12,index=[1,2,3,4,5,6,7])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)

#output 1    24.0
#2    24.0
#3    24.0
#4    24.0
#5     NaN
#6     NaN
#7     NaN
#dtype: flo

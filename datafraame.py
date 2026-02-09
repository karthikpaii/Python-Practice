import pandas as pd

l=[1,2,3,4,5]
var=pd.DataFrame(l)
print(var)


d={"a":[1,2,3,4,5 ],"b":[3,5,6,7,8]}
var1=pd.DataFrame(d,index=["a","b","c","d","f"])
print(var1)

#using list

lis1=[[2,3,4,6],[3,5,8,9]]
var3=pd.DataFrame(lis1)
print(var3)


sr={"s":pd.Series([1,2,3,4],"r":pd.Series[1,2,3,4])}
var3=pd.DataFrame(sr)
print(type(var3))
print(var3)
import pandas as pd
ind=['a','b','c','d','e','f']
y=[1,2,3,4,5,6]
s1=pd.Series(y,index=ind)
print(s1)

#change dtye of series

s2=pd.Series(2,y,dtype='float')
print(s2)

#passing dictionary to series

dic={'name':[1,2,3,4],'name':[3,4,7,8]}
p2=pd.Series(dic)

print(p2)

#single data 
s=pd.Series(2)
print(s)

#concatenTION

pd1=pd.Series([1,2,3,4,6])
pd2=pd.Series([6,5,4,3,2,1])
print(pd1+pd2)


di={'name':'Raja','namee':'Kala','Kas':'Shaym'}
se=pd.Series(di)

print(se)

#access data

print(se[1])
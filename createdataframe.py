import pandas as pd

data=[['Dev','Raj','Krish','Sukhi'],[1,3,4,7]]
df=pd.DataFrame(data)

print(df)

#passing dictionary

dic={"Name":["Dev","Raj","Krish","Veer"],'Age':[20,19,21,23]}
col=['a','B','c','d']
pd2=pd.DataFrame(dic,columns=['Name','Age',"District",'Place'])

print(pd2)

pd2['NEw']=pd2["Name"]
print(pd2)


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
#With two column indices, values same as dictionary keys
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print (df)


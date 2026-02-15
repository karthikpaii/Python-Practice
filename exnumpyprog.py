import numpy as np
list1=[1,2,3]
x=np.array(list1)
print(x)

y=np.array([[3,6,4],[8,9,0]])
print(y)

n=np.array([1,2,3,4,5,6])
n.shape=(3,2)
print(n)

#
m=np.array([2,3,4,5,6,7])
print(np.reshape(m,(3,2)))

#tranpose
y=np.array([[3,6,4],[8,9,0]])
print(np.transpose(y))

#flattening
print(y.flatten())

arr1=np.array([1,2,3])
arr2=np.array([1,2,3])
arr3=np.array([1,2,3])
print(np.concatenate((arr1,arr2,arr3)))

#concatenation
ar1=np.array([[1,2,3],[3,2,4]])
ar2=np.array([[1,2,3],[2,5,6]])
ar3=np.array([[1,2,3],[1,5,6]])
print(np.concatenate((ar1,ar2,ar3),axis=1))

#zeros and ones
print(np.zeros([2,3]))
print(np.ones([2,3]))

#identity marix
print(np.identity(5))

#eye
print(np.eye(5,4,k=-1))

dt = np.dtype('i4')
print (dt)

#arithmetic operations'

y=np.array([[3,2,4],[2,2,5]])
z=np.array([[3,1,4],[2,6,8]])
print(y+z)
print(y-z)

print("sum is",y.sum())
print("min is",y.min())
print("max is",y.max())
print("arg max is",y.argmax())
print("arg min is",y.argmin())
print("mean is",y.mean())

print(y[0][1])

r=np.arange(20)
r.resize(5,5)
print(r)

a = np.array([1.0, 2.0, 3.0])
b = 2.0

print(a * b)

a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a * b)

import pandas as pd
# create a dataframe
df = pd.DataFrame ({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'age': [25, 30, 35, 40],
'city': ['New York', 'Paris', 'London', 'Tokyo']
})
# set the index to the 'name' column
df.set_index('name', inplace=True)
print(df)
print("------------")

s=df.rename(index={'Alice': 'Alicia'}, inplace=True)
print(s)

# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("sample.csv")

# reshape the dataframe using
df_stacked = df.stack()

print(df_stacked.head(26))

import pandas as pd
# making dataframe
df = pd.read_csv("sample.csv")
# unstack() method
df_unstacked =df_stacked.unstack()
print(df_unstacked.head(10))


#melt

# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("sample.csv")

# it takes two columns "Name" and "Team"
df_melt = df.melt(id_vars=['Make','Model'])

print(df_melt.head(10))
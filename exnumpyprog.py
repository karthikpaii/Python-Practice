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
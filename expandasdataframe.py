import pandas as pd

#creating dataframe using list
l1=[1,2,3,4,5]
var=pd.DataFrame(l1)
print(var)

#passing dictionary
dic={"name":['python','css','c++','java'],"numbers":[1,2,3,4], "rank":[1,2,3,4]}
var1=pd.DataFrame(dic)
print(var1)


#passing dictionary [if values are not same then shows error]
dic={"name":['python','css','c++','java'],"numbers":[1,2,3,4], "rank":[1,2,3,4],"c":[1,2,3,4]}
var1=pd.DataFrame(dic)
print(var1)

#output error Traceback (most recent call last):
 # File "c:\Users\Karthik Pai\Documents\Python Practice\Python-Practice\pandasdataframe.py", line 16, in <module>
 # var1=pd.DataFrame(dic)

var1=pd.DataFrame(dic,columns=['name','rank'],index=['a','b','c','d'])
print(var1)
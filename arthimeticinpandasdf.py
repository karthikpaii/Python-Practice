import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
var["C"]=var["A"]+var["B"]
print(var)


#minus
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
var["C"]=var["A"]-var["B"]
print(var)

#logical
var2=pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})
var2["python"]=var2["A"]<=20
print(var2)

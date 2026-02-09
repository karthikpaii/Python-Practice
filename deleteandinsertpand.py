#insert
import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5]})
var.insert(1,"python",var["A"])
print(var)

var["Hello"]=var["A"][:3]
print(var)

var1=var.pop("A")
print(var1)
mport pandas as pd 
def normalize(df): 
return (df - df.min()) / (df.max() - df.min()) 
data = pd.DataFrame({"marks":[50,70,90], "age":[15,16,17]}) 
norm_data = normalize(data) 
print(norm_data) 
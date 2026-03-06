import pandas as pd 
df = pd.DataFrame({"email": ["rahul@gmail.com", "asha@yahoo.com", "john@outlook.com"]}) 
df["domain"] = df["email"].str.split("@").str[1] 
print(df) 


import pandas as pd 
def clean_names(df): 
    names = df["full_name"].str.split(" ", expand=True) 
    df["first_name"] = names[0].str.capitalize() 
    df["last_name"] = names[1].str.capitalize() 
    return df.drop(columns=["full_name"]) 


df = pd.DataFrame({"full_name": ["rahul shetty", "asha kumar"]}) 
print(clean_names(df)) 

import pandas as pd 
df = pd.DataFrame({"date_str": ["2024-01-10", "2024-02-15"]}) 
df["date"] = df["date_str"].apply(lambda x: pd.to_datetime(x)) 
print(df)
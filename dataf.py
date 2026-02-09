import pandas as pd
df=pd.DataFrame(
    { 
        'name':['alice','bob','charlie','david'],
        'age':[25,19,35,40],
         'city':['newtoe','paris','london','tokyo']
    }
)

df.set_index('name',inplace=True)
print(df)



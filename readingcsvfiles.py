import pandas as pd
csv=pd.read_csv('sample.csv')
print(csv)

import pandas as pd
csv2=pd.read_csv('sample.csv',nrows=1)
print(csv2)

print(csv2.index)
print(csv2.columns)
print(csv2.describe())

print(csv.head(10))
print(csv.tail())
print(csv[6:15])
csv.loc[0,"Make"]="Hello"
print(csv)

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

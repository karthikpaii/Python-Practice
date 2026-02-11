#11 questions
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha"],
    "Salary": [60000, 55000, 60000, 65000]
}

df = pd.DataFrame(data)

mean_val = df["Salary"].mean()
median_val = df["Salary"].median()
mode_val = df["Salary"].mode()[0]
std_val = df["Salary"].std()
var_val = df["Salary"].var()

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
print("Standard Deviation:", std_val)
print("Variance:", var_val)


#OUTPUT 
#Mean: 60000.0
#Median: 60000.0
#Mode: 60000
#Standard Deviation: 4082.48290463863
#Variance: 16666666.666666666

#12 question
import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha"],
    "Age": [28, np.nan, 25, 30],
    "Salary": [60000, 55000, np.nan, 65000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Identify missing values
print("\nMissing Values:\n", df.isnull())

# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Drop rows with missing data
df_dropped = df.dropna()

print("\nAfter Filling Missing Values:\n", df)
print("\nAfter Dropping Rows:\n", df_dropped)

#output
#  Original DataFrame:
#     Name   Age   Salary
#0   Amit  28.0  60000.0
#1   Riya   NaN  55000.0
#2  Karan  25.0      NaN
#3   Neha  30.0  65000.0
#
#Missing Values:
#     Name    Age  Salary
#0  False  False   False
#1  False   True   False
#2  False  False    True
#3  False  False   False

#After Filling Missing Values:
#     Name        Age   Salary
#0   Amit  28.000000  60000.0
#1   Riya  27.666667  55000.0
#2  Karan  25.000000  60000.0
#3   Neha  30.000000  65000.0
#
#After Dropping Rows:
#     Name        Age   Salary
#0   Amit  28.000000  60000.0
#1   Riya  27.666667  55000.0
#2  Karan  25.000000  60000.0
#3   Neha  30.000000  65000.0

#13 program
import pandas as pd
df = pd.read_csv("sample.csv")

print("Data Types Before:\n", df.dtypes)

# Convert numeric columns stored as strings
df["Make"] = pd.to_numeric(df["Make"], errors="coerce")
df["Model"] = pd.to_numeric(df["Model"], errors="coerce")

print("\nData Types After:\n", df.dtypes)

#output
#Data Types Before:
# Make      object
#Model     object
#Year     float64
#Price    float64
#dtype: object
#
#Data Types After:
# Make     float64
#Model    float64
#Year     float64
#Price    float64
#dtype: object

#14 program

import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Quantity Sold": [10, 50, 30, 15],
    "Revenue": [500000, 25000, 45000, 150000]
}

df = pd.DataFrame(data)
print("Sales Data:\n", df)

# Total revenue
total_revenue = df["Revenue"].sum()

# Filter products with revenue > 50000
high_revenue = df[df["Revenue"] > 50000]

# Summary report
summary = df.describe()

print("\nTotal Revenue:", total_revenue)
print("\nHigh Revenue Products:\n", high_revenue)
print("\nSummary Report:\n", summary)


#output
#Sales Data:
#     Product  Quantity Sold  Revenue
#0    Laptop             10   500000
#1     Mouse             50    25000
#2  Keyboard             30    45000
#3   Monitor             15   150000
#
#Total Revenue: 720000
#
#High Revenue Products:
#    Product  Quantity Sold  Revenue
#0   Laptop             10   500000
#3  Monitor             15   150000
#
#Summary Report:
#        Quantity Sold        Revenue
#count       4.000000       4.000000
#mean       26.250000  180000.000000
#std        17.969882  220264.991923
#min        10.000000   25000.000000
#25%        13.750000   40000.000000
#50%        22.500000   97500.000000
#75%        35.000000  237500.000000
#max        50.000000  500000.000000


#15
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [60000, 55000, 50000, 65000]
}

df = pd.DataFrame(data)

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

#output
#Department
#Finance    65000.0
#HR         55000.0
#IT         55000.0
#Name: Salary, dtype: float64

#16th ques
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Array:\n", arr)

row_sum = arr.sum(axis=1)
col_mean = arr.mean(axis=0)

print("Row-wise Sum:", row_sum)
print("Column-wise Mean:", col_mean)

#output
#Array:
# [[10 20 30]
# [40 50 60]
# [70 80 90]]
#Row-wise Sum: [ 60 150 240]
#Column-wise Mean: [40. 50. 60.]


#17 question
import numpy as np

arr = np.random.randint(1, 100, 10)
print("Array:", arr)

threshold = 50
filtered = arr[arr > threshold]

print("Elements > 50:", filtered)

#output

#Array: [99 80 18 81 91 95 47 94  8 73]
#Elements > 50: [99 80 81 91 95 94 73]

#18 program
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
result = A@B
#result=np.dot(A,B)
res=A*B
print("Element Wise Multiplication",res)
print(result)
# or: result = A @ B

print("Matrix Multiplication:\n", result)
#output
#Element Wise Multiplication [[ 5 12]
# [21 32]]
#[[19 22]
# [43 50]]
#Matrix Multiplication:
# [[19 22]
# [43 50]]


#19 question
import pandas as pd

data = {
    "Date": ["2024-01-10", "2024-02-15", "2024-03-20"],
    "Sales": [2000, 3500, 2800]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print(df)


#output
#       Date  Sales  Year  Month  Day
#0 2024-01-10   2000  2024      1   10
#1 2024-02-15   3500  2024      2   15
#2 2024-03-20   2800  2024      3   20


#20 question

import pandas as pd

df1 = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Amit", "Riya", "Karan", "Neha"]
})

df2 = pd.DataFrame({
    "EmpID": [3, 4, 5],
    "Salary": [50000, 60000, 55000]
})

# Inner join
inner_join = pd.merge(df1, df2, on="EmpID", how="inner")

# Left join
left_join = pd.merge(df1, df2, on="EmpID", how="left")

# Right join
right_join = pd.merge(df1, df2, on="EmpID", how="right")

print("Inner Join:\n", inner_join)
print("\nLeft Join:\n", left_join)
print("\nRight Join:\n", right_join)

#output:
#Inner Join:
#    EmpID   Name  Salary
#0      3  Karan   50000
#1      4   Neha   60000
#
#Left Join:
#    EmpID   Name   Salary
#0      1   Amit      NaN
#1      2   Riya      NaN
#2      3  Karan  50000.0
#3      4   Neha  60000.0
#
#Right Join:
#    EmpID   Name  Salary
#0      3  Karan   50000
#1      4   Neha   60000
#2      5    NaN   55000
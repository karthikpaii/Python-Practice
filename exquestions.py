#ques 1
import numpy as np

int_arr = np.array([1, 2, 3, 4], dtype=int)
float_arr = np.array([1.5, 2.7, 3.2], dtype=float)
complex_arr = np.array([1+2j, 3+4j, 5+6j], dtype=complex)

print("Integer Array:", int_arr, int_arr.dtype)
print("Float Array:", float_arr, float_arr.dtype)
print("Complex Array:", complex_arr, complex_arr.dtype)
#output:Integer Array: [1 2 3 4] int64
#Float Array: [1.5 2.7 3.2] float64
#Complex Array: [1.+2.j 3.+4.j 5.+6.j] complex128

#ques2
import numpy as np

arr = np.random.randint(1, 21, size=(4, 4))
print("Original Array:\n", arr)

# Access elements
print("Element at (1,2):", arr[1, 2])
print("First row:", arr[0])
print("Second column:", arr[:, 1])
print("Sub-matrix (first 2 rows & columns):\n", arr[:2, :2])

# Modify elements
arr[0, 0] = 99
arr[:, 3] = 0

print("Modified Array:\n", arr)

a = np.array([1,2,3])
b = 10
print(a + b)   # [11 12 13]
#output:Original Array:
# [[19  5 17  6]
# [ 9  7  3 12]
# [20  5 14 10]
# [12  2 12  3]]
#Element at (1,2): 3
#First row: [19  5 17  6]
#Second column: [5 7 5 2]
#Sub-matrix (first 2 rows & columns):
# [[19  5]
# [ 9  7]]
#Modified Array:
# [[99  5 17  0]
# [ 9  7  3  0]
# [20  5 14  0]
# [12  2 12  0]]

#question3

import numpy as np

def array_operations(a, b):
    return a + b, a - b, a * b

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

sum_arr, diff_arr, prod_arr = array_operations(x, y)

print("Sum:", sum_arr)
print("Difference:", diff_arr)
print("Product:", prod_arr)
#output: Sum: [5 7 9]
#output: Difference: [-3 -3 -3]
#output: Product: [ 4 10 18]

#question4
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Square root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Natural log:", np.log(arr))
#output: Square root: [1.         1.41421356 1.73205081 2.         2.23606798]
#Exponential: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
#Natural log: [0.         0.69314718 1.09861229 1.38629436 1.60943791]

#question5
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([25, 15, 35, 5])

print("Maximum:", np.max(a))
print("Minimum:", np.min( b))
#output:Maximum: 40
#Minimum: 5


#ques 6

import numpy as np

# Create array of 20 random floats
arr = np.random.rand(20) * 100
print("Original Float Array:\n", arr)

# Function to convert
def convert_types(a):
    int_arr = a.astype(int)
    bool_arr = a.astype(bool)
    return int_arr, bool_arr

int_array, bool_array = convert_types(arr)

print("\nInteger Array:\n", int_array)
print("\nBoolean Array:\n", bool_array)

#output:Original Float Array:
#[34.24406726 80.00488582 45.05124034 39.20982604 41.57078291 32.91779992
#11.58974535 96.01238442 10.91591608 42.51495146 38.8319622  27.57676935
#31.51701269 31.17939347 66.5977629  71.08365419 55.24611417 46.88613906
# 7.29881842 24.09540752]
#Integer Array:
#[34 80 45 39 41 32 11 96 10 42 38 27 31 31 66 71 55 46  7 24]
#Boolean Array:
#[ True  True  True  True  True  True  True  True  True  True  True  True
# True  True  True  True  True  True  True  True]

#ques 7 flattening
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)

flat = arr.flatten()
print("Flattened Array:", flat)

reshaped = flat.reshape(arr.shape)
print("Reshaped Back:\n", reshaped)


#output:Original Array:
# [[1 2 3]
# [4 5 6]]
#Flattened Array: [1 2 3 4 5 6]
#Reshaped Back:
# [[1 2 3]
# [4 5 6]]


#8 question

import numpy as np

arr = np.array([10, 20, 30, 40])
scalar = 5

result = arr + scalar
print("Result:", result)
#output Result: [15 25 35 45]

#9th
import pandas as pd

data = {
    "Name": ["Ravi", "Anita", "John", "Meena"],
    "Age": [25, 28, 22, 30],
    "City": ["Delhi", "Mumbai", "Chennai", "Pune"]
}

df = pd.DataFrame(data)
print(df.head())


#output:
#    Name  Age     City
#0   Ravi   25    Delhi
#1  Anita   28   Mumbai
#2   John   22  Chennai
#3  Meena   30     Pune


#10th
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Karan", "Neha"],
    "Age": [28, 32, 25, 30],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [60000, 55000, 50000, 65000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add bonus column (10% of salary)
df["Bonus"] = df["Salary"] * 0.10

# Filter by department
it_employees = df[df["Department"] == "IT"]

# Sort by salary
sorted_df = df.sort_values(by="Salary")

print("\nWith Bonus Column:\n", df)
print("\nIT Department Employees:\n", it_employees)
print("\nSorted by Salary:\n", sorted_df)

#output  Original DataFrame:
#     Name  Age Department  Salary
#0   Amit   28         IT   60000
#1   Riya   32         HR   55000
#2  Karan   25         IT   50000
#3   Neha   30    Finance   65000
#
#With Bonus Column:
#     Name  Age Department  Salary   Bonus
#0   Amit   28         IT   60000  6000.0
#1   Riya   32         HR   55000  5500.0
#2  Karan   25         IT   50000  5000.0
#3   Neha   30    Finance   65000  6500.0
#
#IT Department Employees:
#     Name  Age Department  Salary   Bonus
#0   Amit   28         IT   60000  6000.0
#2  Karan   25         IT   50000  5000.0
#
#Sorted by Salary:
#     Name  Age Department  Salary   Bonus
#2  Karan   25         IT   50000  5000.0
#1   Riya   32         HR   55000  5500.0
#0   Amit   28         IT   60000  6000.0
#3   Neha   30    Finance   65000  6500.0


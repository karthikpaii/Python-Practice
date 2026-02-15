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
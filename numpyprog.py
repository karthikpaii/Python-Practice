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
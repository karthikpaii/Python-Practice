import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 50)
y = np.sin(x)

np.random.seed(0)
scatter_x = np.random.rand(50)
scatter_y = np.random.rand(50)

hist_data = np.random.randn(1000)

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Create figure and subplots (2 rows, 2 columns)
plt.subplot(2,2,1)

# ---------------- Line Plot ----------------

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("sin(X)")



# ---------------- Scatter Plot ----------------
plt.subplot(2,2,2)
plt.scatter(scatter_x, scatter_y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

# ---------------- Histogram ----------------
plt.subplot(2,2,3)
plt.hist(hist_data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")

# ---------------- Bar Chart ----------------
plt.subplot(2,2,4)
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display
plt.show()
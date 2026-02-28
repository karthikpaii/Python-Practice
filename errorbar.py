import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y = [2.0, 2.5, 3.0, 3.5, 4.0]
error = [0.2, 0.30, 0.28, 0.3, 0.2]
# Plot with error bars
plt.errorbar(x, y, yerr=error, fmt='o-', capsize=5, color='blue')
plt.xlabel("X Values")
plt.ylabel("Measurements")
plt.title("Line Plot with Error Bars")
plt.grid(True)
plt.show()
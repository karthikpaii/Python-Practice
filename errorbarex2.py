import numpy as np
import matplotlib.pyplot as plt
data = [10, 12, 9, 11, 13, 10, 12, 11]
mean = np.mean(data)
std_dev = np.std(data)
x = [1]
plt.errorbar(x, [mean], yerr=[std_dev], fmt='o',
ecolor='red', capsize=10, capthick=2)
plt.xticks([1], ["Dataset"])
plt.ylabel("Values")
plt.title("Mean with Standard Deviation Error Bar")
plt.show()
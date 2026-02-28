import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,45,33,22,37,36,31,27,18,13,18,8])
y=[10,20,30,40,50]
plt.hist(x,y,ec="k")
plt.show()
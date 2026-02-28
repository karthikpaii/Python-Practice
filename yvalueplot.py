import matplotlib.pyplot as plt
import numpy as np

a=[1,2,3,4]
plt.xlabel("X label")
plt.ylabel("Y Label")
plt.plot(a,linestyle="dotted",marker="*", markeredgecolor="red",markersize=13)
plt.legend("His")
plt.show()
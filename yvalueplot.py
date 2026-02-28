import matplotlib.pyplot as plt
import numpy as np

a=[1,2,3,4]
plt.xlabel("X label")
plt.ylabel("Y Label")
plt.plot(a)
plt.plot([10,20,30,40],linewidth=2,alpha=0.5)
plt.legend(["sq","ss"])
plt.show()
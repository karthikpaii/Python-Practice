#Write a Python script using Matplotlib to create a multi-panel plot with 2 rows and 2 columns.
#Each subplot should display a different type of plot (e.g., line plot, scatter plot, histogram, bar
#chart).

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([3,4,5,6])

hi1=np.array([1,2,3,20,10,33,45,26,47,48])
bi=[10,20,30,40,50]

b1=["Science","Commerce","Maths"]
std=[100,200,400]

plt.subplot(2,2,1)
plt.plot(x,y)
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Line Plot")

plt.subplot(2,2,2)
plt.scatter(x,y)
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Scatter Plot")


plt.subplot(2,2,3)
plt.hist(hi1,bins=bi,ec="k",color='red')
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Scatter Plot")


plt.subplot(2,2,4)
plt.bar(b1,std,color='red')
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Scatter Plot")

plt.show()
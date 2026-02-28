import matplotlib.pyplot as plt
import numpy as np

x=np.array([40,20,10,30])
y=["Tea","coffe","tea3","Vim"]
plt.pie(x,labels=y,autopct="%0.1f%%",explode=[0,0.3,0,0])
plt.show()
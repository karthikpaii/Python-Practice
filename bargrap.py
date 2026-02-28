import matplotlib.pyplot as plt
#horizontal bar 
x=["Science","Comerce","Arts"]
y=[300,200,100]

d=["Hi","HI","Hello"]
plt.barh(x,y,height=0.8,color="red",align="edge",ec="k")
plt.xlabel("Stream")
plt.ylabel("No of Course")
plt.show()


x=["Science","Comerce","Arts"]
y=[300,200,100]


#vertical bar 
d=["Hi","HI","Hello"]
plt.bar(x,y,height=0.8,color="red",align="edge",ec="k")
plt.xlabel("Stream")
plt.ylabel("No of Course")
plt.show()
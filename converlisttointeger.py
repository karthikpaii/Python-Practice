#Create a Python program that takes two lists of integers, converts them into sets, and prints the 
#union and intersection of these sets. Explain how sets can be used to handle unique data.

lis=[1,2,3,4,5]
lis2=[3,4,5,6,7]

set1=set(lis)
set2=set(lis2)


print("union of Set1 and set 2 is:", set1.union(set2))
print("iNtersection of Set1 and set 2 is:", set1.intersection(set2))
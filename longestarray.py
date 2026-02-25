arr=[1,2,3,4,5]
k=2
count=0
c2=0
res=[]
for ele in arr:
    if ele>k:
        count=count+1
        res.append(ele)
    else:
        c2=c2=1
        res.append(ele)
if(count>=c2):
    print(count)
else:
    print()

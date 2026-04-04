i=0
strs = ["flower","flow","flight"]
s=sorted(strs)
n=len(s)

first=s[0]
last=s[n-1]
res=""
s=""
for  i in range(0,n):
    if first[i]!=last[i]:
        break
    res+=first[i]
    

print(res)

 
       
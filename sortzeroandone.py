class Solution:
    def sort012(self,arr, n) :
        a=[]
        for i in range(n):
            a.append(arr[i]) 
            a.sort()
        return a

ar=[0,1,2,2,1,0]  
n=6
c=Solution()
print(c.sort012(ar,n))

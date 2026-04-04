class Solution:
    def reverseArray(self,arr, m):
        n=len(arr)
        new=[]
        a=[]
        for i in range(0,m+1):
           new.append(arr[i])
        
        for i in range(m+1,n):
             a.append(arr[i])
        s=a.reverse()
        
        for i in a:
         new.append(i)
            

        return new
            
            
 
    

ar=[1,2,3,4,5,6]
m=3
c=Solution()
print(c.reverseArray(ar,m))
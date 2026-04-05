class Solution:
    def getSecondLargest(self, arr):
        s=arr.sort()
        lar=arr[0]
        
        for i in range(len(arr)):
            if arr[i]>=lar:
                return lar
            
c=Solution()
a=[12,1,23,17,19]
print(c.getSecondLargest(a))

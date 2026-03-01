class Solution:
	def pushZerosToEnd(self, arr):
        i=0
        for j in range(len(arr)-1):
            if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
		return arr
				
a= [1, 2, 0, 4, 3, 0, 5, 0]
c=Solution()
print(c.pushZerosToEnd(a))
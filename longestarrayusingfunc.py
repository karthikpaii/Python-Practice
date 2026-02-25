class Solution:
    def longestSubarray(self, arr, k):
        
        for ele in arr:
            if ele>=k:
                count=count+1
            
            else:
                c2=c2+1
        return count, c2
    
if(count>=c2):
    print(count)
else:
    print(c2)

count=0
c2=0         
ar=[1,2,3,4,1]
ele=2
c=Solution()
print(c.longestSubarray(ar,ele))



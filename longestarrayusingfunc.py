class Solution:
    def longestSubarray(self, arr, k):
        leng=0
        res={}
        count=0
        for i in range(len(arr)):
            if arr[i]>k:
                count=count+1
            else:
                count=count-1

            if count>0:
                leng=i+1
            
            if count not in res:
                res[count]=i
            
            if(count-1) in res:
                leng=max(leng,i-res[count-1])
        return leng
c2=0         
ar=[1,2,3,4,1]
ele=2
c=Solution()
print(c.longestSubarray(ar,ele))



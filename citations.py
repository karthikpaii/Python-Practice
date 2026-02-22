class Solution:
    def hIndex(self, citations):
       citations.sort(reverse=True)
       
       count=0
       for i in range(len(citations)):
          
           if citations[i]>=i+1:
               count=count+1
           else:
               break
       return count

arr= [0,0]
new=Solution()
print(new.hIndex(arr))

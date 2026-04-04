class Solution(object):
    def combinationSum(self, candidates, target):
         n=len(candidates)
         res=[]
         for i in range(n):
           for j in range(i+1,n):
                if candidates[i]+candidates[i+1]==target:
        
                 return [i,j]







candi=[2,3,6,7]
tar=7
c=Solution()
print(c.combinationSum(candi,tar))
        
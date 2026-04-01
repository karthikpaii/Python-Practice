class Solution(object):
    def containsDuplicate(self, nums):
      for i in nums:
        for j in nums:
            if nums[i]==nums[j]:
                return False
        
        return True
      

num=[1,2,3,3]
c=Solution()
print(c.containsDuplicate(num))


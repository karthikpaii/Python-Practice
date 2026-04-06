class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # position for unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
        
ar = [1,1,2]
a=[1,2,3,4,1,2,3,4]
c=Solution()
print(c.removeDuplicates(ar))
print(c.removeDuplicates(a))
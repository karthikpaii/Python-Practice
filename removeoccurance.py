
class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # position for next valid element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k

nums = [3,2,2,3]
val = 3
c=Solution()
print(c.removeElement(nums,val))
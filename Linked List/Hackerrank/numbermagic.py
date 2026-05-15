class Solution(object):
    def firstUniqueEven(self, nums):
        
        number=set(nums)
        for num in number:
            if num%2==0:
                if num not in new:
                    new.append(num)
            else:
                return -1
        return len(new)
    
nums = [4,4]
c=Solution()
print(c.firstUniqueEven(nums))
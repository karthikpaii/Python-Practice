class Solution(object):
    def firstUniqueEven(self, nums):
        new = []
        repeat = []

        for num in nums:
            if num % 2 == 0:
                if num not in new and num not in repeat:
                    new.append(num)
                elif num in new:
                    new.remove(num)
                    repeat.append(num)

        if not new:
            return -1
        else:
            return new[0]
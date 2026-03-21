class Solution(object):
    def plusOne(self, digits):
        y="".join(map(str, digits))
        dig=int(y)
        num=dig+1
        digi=  [int(digits) for digits in str(num)]
        return digi


digit=[1,2,3]
c=Solution()
print(c.plusOne(digit))
        
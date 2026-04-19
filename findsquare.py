class Solution:
    def isPower(self, x, y):
        
        for i in range(1,100):
            if pow(x,i)==y:
                return True
                
        return False


x=1
y=8
c=Solution()
print(c.isPower(x,y))
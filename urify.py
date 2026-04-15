class Solution:
    def URLify(self, s):
       res=s.strip()
       n=res.replace(" ","%")
       return n
        
        
sm= "i love programming"
c=Solution()
print(c.URLify(sm))
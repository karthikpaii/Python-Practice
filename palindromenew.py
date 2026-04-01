import re
class Solution(object):
    def isPalindrome(self, s):
       result = re.sub(r'[^a-zA-Z0-9\s]', '', s)
       res1=result.replace(" ","")
       res=res1.lower()
       re1=res[::-1]
       print(res1)
       print(re1)
       if res==re1:
           return True
       else:
            return False
          
       
        



m= "A man, a plan, a canal: Panama"
c=Solution()
print(c.isPalindrome(m))
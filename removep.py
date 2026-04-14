class Solution:
    def removeSpaces(self, s):
        m = []   
        
        for i in s:
            if i != " ":
                m.append(i)
        
        return "".join(m)   


m = "g eeks for ge eks"
c = Solution()
print(c.removeSpaces(m))
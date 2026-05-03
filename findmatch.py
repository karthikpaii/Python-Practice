class Solution:
    def smallestSubstring(self, s):
        # code here
        arr=[]
        for i in range(len(s)):
            if s[i]=='0' or s[i]=='1' or s[i]=='2' not in arr:
                arr.append(s[i])
            
            else:
                return -1
                
        return len(arr)

s = "102121"
c=Solution()
print(c.smallestSubstring(s))
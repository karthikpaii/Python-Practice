class Solution:
    def largestSwap(self, s):
       c=list(s)
       n=len(s)
       if n==2:
           return s
       else:
            temp=c[0]
            c[0]=c[n-1]
            c[n-1]=temp
            res=''.join(str(item) for item in c)
            return res

s="93"
c=Solution()
print(c.largestSwap(s))
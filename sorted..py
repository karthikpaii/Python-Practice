class Solution:
    def intersectionn(self,a, b):
        res = list(set(a).intersection(set(b)))
        res.sort()
        return res


a= [5,1, 1, 2, 2, 2,4, ]
b = [2, 2, 4, 5]
c=Solution()
print(c.intersectionn(a,b))
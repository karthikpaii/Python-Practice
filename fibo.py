class Solution(object):
     a=0
     b=1
     def fib(self, n):
        for i in range(n):
           c=a+b
           a,b =b,c
           return c
               



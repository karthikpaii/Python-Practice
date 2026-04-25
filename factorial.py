# Create a function for factorial
def factorial(n):
   fact=1
   for i in range(1,n+1):
      fact*=i
   return fact


# Read input and print result
num = int(input())
print(str(num) + "! = " + str(factorial(num)))

#2 Write safe arithmetic calculator program. Input num1, operator, num2. Use if-elif for +,-,*,/.
#Handle ZeroDivisionError and ValueError with try-except. Print result type.

a=int(input("Enter a Number 1:"))
op=input("Enter a Operator:")
b=int(input("Enter a Number 2:"))
if(op=='+'):
    c=a+b
    print(c)
elif (op=='*'):
    c=a*b
    print(c)
elif (op=='-'):
    c=a-b
    print(c)
elif (op=='/'):
    if b==0:
        print("Devision By Zero")
    else:
        c=a/b
        print(c)
else:
    print("wrong Operator")

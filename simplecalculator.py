n1=int(input("Enter a First Number:"))
op=input("Enter a Operator:")
n2=int(input("Enter the second Number:"))

if op=='+':
    r=n1+n2
    print("Result",r)
elif op=='-':
    r=n1-n2
    print("Result",r)
elif op=='*':
    r=n1*n2
    print("Result",r)
else:
    if n2!=0:
        c=n1/n2
        print("Result",r) 
    else:
        print("Error While Devision")


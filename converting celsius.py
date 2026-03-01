print("1. Celsius to fareheit")
print("1.  fareheit to Celsius")

ch=int(input("Enter Your Choice:"))

if ch==1:
    c=int(input("Enter celsuus"))
    f=(c*9/5)+32
    print("Celsuius",f)

elif ch==2:
    f=int(input("Enter Fareheint"))
    c=(f-32)*5/9

else:
    print("invalid")
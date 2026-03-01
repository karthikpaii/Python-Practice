n=int(input("Enter a Number:"))

if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime NUmber")
            break
    else:
          print("Its a PRime Number")

else:
    print("not A Prime  Number")
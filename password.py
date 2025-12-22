n=input("Enter a PAssword: ")
if(len(n)>8):
   
    if any(char.isupper() for char in n):
       if any(dig.isdigit() for dig in n):
              print("Good Password")
       else:
          print("At Least one Digit Should be There")
    else:
        print("atleast one char should be uppercase")
else:
    print("password Must be >8")



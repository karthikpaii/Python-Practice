year=int(input("Enter a Year:"))

if(year%4==0 and year%100!=0) or (year%400==0):
    print("Its a Leap Year")
else:
    print("Not a Leap YEar")
n=input("Enter a Elemens sep by space").split()

total=0
for num in n:
    if num.isdigit():
        total=total+int(num)

print("Total Elements are:",total)
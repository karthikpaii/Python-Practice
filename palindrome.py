# Reversing a list
numbers = 123
num=str(numbers)
rev=int(''.join(reversed(num)))
if(numbers==rev):
    print("good thing")
    print(rev)
else:
    print("wrong")
    print(rev)

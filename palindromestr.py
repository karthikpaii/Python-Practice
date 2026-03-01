
while(True):
    n=int(input("Enter a String: "))
    if n==n[::-1]:
        print("palindrome")
    else:
        print("Not a Palindrome")
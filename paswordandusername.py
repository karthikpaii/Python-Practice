passw="1234"
user="admin123"

for attempt in range(1,4):
    us=input("Enter a User Name")
    pa=input("Enter a PAssword")
    if us==user and pa==passw:
        print("Login Succesfull")
        break
    else:
        print("Wrong Password")

else:
    print("Account Locked Too MAny Attempts")
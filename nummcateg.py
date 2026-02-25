while(True):
    num = int(input("Enter a number: "))
    if num == 0:
        print("The number is Zero")
    else:
        if num > 0:
            if num % 2 == 0:
                print("Positive Even")
            else:
                print("Positive Odd")
        else:
            if num % 2 == 0:
                print("Negative Even")
            else:
                print("Negative Odd") 
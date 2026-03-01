x=10

def glob():
    global x
    print("Inside x value",x)
glob()

print("outside x value",x)
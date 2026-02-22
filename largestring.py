arr=[3, 30, 34, 5, 9]
arr = list(map(str, arr))


def comapre(a,b):
    if (a+b>b+a):
        return a+b
    elif(a+b<b+a):
        return b+a
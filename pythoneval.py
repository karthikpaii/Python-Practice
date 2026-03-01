def evaluation(n):
    exp="0123456789+-* / % // **"
    for num in n:
        if num not in exp:
            return False
    return True


exp=input("Enter a Expression")

if evaluation(exp):
    try:
        result=eval(exp)
        print(result)
    except ZeroDivisionError:
        print("invaliid")
    except Exception:
        print("ivalid String")


else:
    print("inbalid Chars")
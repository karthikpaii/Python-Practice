
def is_valid(expr):
    valid_ch="0123456789+-*/()"

    for ch in expr:
        if ch not in valid_ch:
            return False
        return True
        
exp=input("Enter a Expression")

if is_valid(exp):
    try:
        res=eval(exp)
        print(res)
    except ZeroDivisionError:
        print("devision By Zero")

    except Exception:
        print("Invalid Expression")

else:
    print("Invalid Characters")
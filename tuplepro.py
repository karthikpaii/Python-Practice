
def calculate(n):
    n2=[]
    for ele in n[1::2]:
        n2.append(ele)
        n3=tuple(n2)
    return n3

num=(1,2,3,4,5,6,7,8,9,10,11,12)
res=calculate(num)
print(res)
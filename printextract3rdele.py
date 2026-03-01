def removeele(li,ele):
    for num in li:
        if ele==num:
           li.remove(ele)

    return li

lis=[1,2,3,4,5,3,6,5]
el=5

res=removeele(lis,el)
print(res)
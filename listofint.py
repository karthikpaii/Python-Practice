def counting(numb):
    freq={}
    for num in numb:
        if num in freq:
            freq[num]=freq[num]+1
        else:
            freq[num]=1

    return freq
nums=list(map(int,input("Enter a Number by Space").split()))

res=counting(nums)
print(res)

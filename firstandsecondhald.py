def stringman(s):
    mid=len(s)//2
    first=s[:mid][::-1]
    second=s[mid:]
    return first+second
    

st="python"
re=stringman(st)
print(re)
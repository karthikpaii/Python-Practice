n=[2,3,4,5,6,7,8,9,10,13,14,16,18,19,39,40,50]

for num in n:
    if num>20:
        break
    
    if num%2!=0:
        continue
    print(num,end=" ")

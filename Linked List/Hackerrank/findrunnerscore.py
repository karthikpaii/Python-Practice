if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    lis=[]
    for i in range(len(arr)):
        lis.append(arr[i])
        
    arr = list(set(arr))   
    arr.sort()             
    print(arr[-2]) 
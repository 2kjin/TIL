import math
n=int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    res = 0
    for j in range(1,len(arr)):
        for k in range(j+1,len(arr)):
            res += math.gcd(arr[j],arr[k])
    print(res)
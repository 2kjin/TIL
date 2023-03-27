T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    res = 0
    s = n //2
    e = n //2
    c = n //2
 
    for i in range(n):
        for j in range(s, e+1):
            res += arr[i][j]
        if i < c:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
 
    print(f'#{t} {res}')
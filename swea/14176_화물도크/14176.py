T = int(input())
for t in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: x[1])
 
    result = 1
    end = lst[0][1]
    for i in range(n):
        if lst[i][0] >= end:
            result += 1
            end = lst[i][1]
 
    print(f'#{t} {result}')
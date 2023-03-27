import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    c = n//2

    change = -1
    res = 0

    for i in range(n):
        if i >= c:
            change = 1
        for j in range(abs(i-c), abs(n-c)):
            res += arr[i][j]
        c += change
    print(f'#{t} {res}')
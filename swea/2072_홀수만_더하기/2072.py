import sys
sys.stdin = open('2072input.txt')

T = int(input())
ans = 0

for tc in range(1,T+1):
    n = list(map(int,input().split()))

    for i in n:
        if i // 2 == 0:
            ans += i

    print(ans)
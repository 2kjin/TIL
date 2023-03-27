import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    a = int(input())
    b = list(map(int, input().split()))

    for i in range(a - 1, 0, -1):
        for j in range(0, i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]

    print(f'#{tc+1} ', end='')
    print(*b)
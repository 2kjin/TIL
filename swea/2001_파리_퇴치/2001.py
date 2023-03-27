import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    N = [list(map(int, input().split())) for _ in range(a)]

    result = 0
    for i in range(a - b + 1):
        for j in range(a - b + 1):
            sums = 0
            for k in range(i,i+b):
                for l in range(j,j+b):
                    sums += N[k][l]
            if sums > result:
                result = sums

    print(f'#{t} {result}')
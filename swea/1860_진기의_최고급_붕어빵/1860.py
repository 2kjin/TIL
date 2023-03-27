import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int,input().split())
    p = list(map(int,input().split()))
    result = 'Possible'
    p.sort()
    # for i in range(N-1,0,-1):
    #     for j in range(0,i):
    #         if p[j] > p[j+1]:
    #             p[j], p[j+1] = p[j+1], p[j]

    for i in range(N):
        if p[i] // M * K - i > 0:
            result
        else:
            result = 'Impossible'
            break

    print(f'#{t} {result}')
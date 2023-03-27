import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    for i in range(N):
        n = int(input())

        print(f'#{t} {n}')

import sys
sys.stdin = open('13755input.txt')

T = int(input())
for t in range(1, T + 1):
    a, b = map(int,input().split())
    # lst = input().split()
    # a = int(lst[0])
    # b = int(lst[1])

    # arr = [list(map(str,input())) for _ in range(a)]
    arr = [input() for _ in range(a)]
    result = []

    for n in range(N):
        for m in range(N - M + 1):
            if lst[n][m: m + M] == lst[n][m: m + M][::-1]:
                print(f'#{t + 1}', ''.join(lst[n][m: m + M]))

    for n in range(N):
        for m in range(N - M + 1):
            if lst_reverse[n][m: m + M] == lst_reverse[n][m: m + M][::-1]:
                print(f'#{t + 1}', ''.join(lst_reverse[n][m: m + M]))

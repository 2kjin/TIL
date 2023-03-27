T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = [0] + list(map(int, input().split())) + [N]
 
    start = stop = 0
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > K:
            stop = 0
            break
        if lst[i] - lst[start] > K:
            start = i - 1
            stop += 1
    print(f'#{t} {stop}')
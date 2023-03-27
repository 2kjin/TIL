T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
  
    N = int(input())
    prelst = [0, 1]
    for n in range(1, N+1):
        lst = [0] * n
        for i in range(n):
            lst[i] = prelst[i] +prelst[i+1]
        print(*lst)
        prelst = [0] + lst + [0]
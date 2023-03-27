T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
      
    for i in range(1, N):
        lst[0][i] += lst[0][i-1]
        lst[i][0] += lst[i-1][0]
  
    for i in range(1, N):
        for j in range(1, N):   
            y = lst[i-1][j]
            x = lst[i][j-1]
            if x > y:
                lst[i][j] += y
            else:
                lst[i][j] += x
 
    print(f'#{t}', lst[N-1][N-1])
T = int(input())
 
for t in range(1,1+T):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
     
       # 상 하 좌 우
    dr= [-1 ,1, 0, 0]
    dc= [ 0, 0,-1, 1]
 
    res = 0
    for i in range(N):
        for j in range(N):
            arr_sum = 0
            r = i
            c = j
            arr_sum += arr[r][c]
            for k in range(4):
                for l in range(1, M):
                    nr = r + dr[k]*l
                    nc = c + dc[k]*l
                    if 0 <= nr < N and 0 <= nc < N:
                        arr_sum += arr[nr][nc]
            if res < arr_sum:
                res = arr_sum
                 
        #좌상 우상 좌하 우하
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
 
    for i in range(N):
        for j in range(N):
            arr_sum = 0
            r = i
            c = j
            arr_sum += arr[r][c]
            for k in range(4):
                for l in range(1, M):
                    nr = r + dr[k] * l
                    nc = c + dc[k] * l
                    if 0 <= nr < N and 0 <= nc < N:
                        arr_sum += arr[nr][nc]
            if res < arr_sum:
                res = arr_sum
            # 1. N만큼 더미
            # 2. 범위를 넘어가면 하지않게 if 문
 
    print(f'#{t} {res}')
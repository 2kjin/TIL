T = int(input())
 
for t in range(1,T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
 
    o_arr = []
    cnt = 0
    res = 'NO'
    for i in arr:
        for j in i:
            o_arr.append(list(j))
    # 가로 오목
    for I in range(N):
        for J in range(N):
            if o_arr[I][J] == '.':
                break
        else:
            res = 'YES'
            break
 
    # 세로 오목
    for I in range(N):
        for J in range(N):
            if '.' in o_arr[J][I]:
               break
        else:
            res = 'YES'
            break
     
    #우하단 오목
    for I in range(N):
        if '.' in o_arr[I][I]:
            break
    else:
        res = 'YES'
 
    #좌하단 오목
    for I in range(N):
        if o_arr[I][N-1-I] == '.':
            break
    else:
        res = 'YES'   
 
    print(f'#{t} {res}')
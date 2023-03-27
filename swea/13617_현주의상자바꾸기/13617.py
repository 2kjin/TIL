T = int(input())
 
for t in range(1,T+1):
    N, Q = map(int,input().split())
    LR_lst = []
    box = [0] * (N+1)
    for _ in range(1,Q+1):
        L, R = map(int,input().split())
        LR_lst.append((L, R))
 
    for i in range(Q):
        for j in range(LR_lst[i][1]-LR_lst[i][0]+1):
            box[j+LR_lst[i][0]] = i+1
         
    sol = []
    for k in range(1,len(box)):
        sol.append(box[k])
print(f'#{t}', *sol)
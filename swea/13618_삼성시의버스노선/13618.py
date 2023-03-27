T = int(input())
 
for t in range(1,T+1):
    N = int(input())
    lst_bus = []
    for _ in range(1, N+1):
        a, b = map(int,input().split())
        lst_bus.append((a,b))
    P = int(input())
    station = [0]*P
    c_lst = [list(map(int,input().split())) for _ in range(P)]
 
    for i in lst_bus:
        a,b = i
        for j in range(a-1, b):
            station[j] += 1
    print(f'#{t}',*station)
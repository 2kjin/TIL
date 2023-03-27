T = int(input())
 
for t in range(1,T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
 
    max_value = 0
    min_value = 1000001
 
    for i in range(N-M+1):
        a_sum = 0
        for j in range(M):
            a_sum += a[i+j]
 
        if a_sum > max_value:
            max_value = a_sum
        if a_sum < min_value:
            min_value = a_sum
             
     
    print(f'#{t} {max_value - min_value}')
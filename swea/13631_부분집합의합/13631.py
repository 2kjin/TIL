T = int(input())
 
for case in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(range(1, 13))
    m=len(arr)
    ans = 0
     
    for i in range(1<<m):
        cnt = 0
        sum = 0
        for j in range(m):
            if i & (1<<j):
                sum += arr[j]
                cnt += 1
        if cnt == N and sum == K:
            ans += 1
             
    print(f'#{case} {ans}')
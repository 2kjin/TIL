n, k = map(int, input().split())
s = list(map(int, input().split()))

end = 0
res = 0
tmp = 0
cnt = 0

for i in range(n):
    while (cnt <= k and end < n):     
        if s[end] % 2 == 1:
            cnt += 1
        else:
            tmp += 1
        end += 1
        if i == 0 and end == n:
            res = tmp
            break
    if cnt == k+1 :
        res = max(tmp, res)
        
    if s[i] %2 == 1:
        cnt -= 1
    else:
        tmp -= 1
        
print(res)
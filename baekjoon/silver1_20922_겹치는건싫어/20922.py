n, k = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
l, r = 0, 0
cnt = [0] * (max(lst) + 1)

while r < n:
    if cnt[lst[r]] < k:
        cnt[lst[r]] += 1
        r += 1
    else:
        cnt[lst[l]] -= 1
        l += 1
    ans = max(ans, r - l)
print(ans)
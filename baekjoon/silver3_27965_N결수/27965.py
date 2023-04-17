n, k = map(int, input().split())

res = 0
for i in range(1, n+1):
    res = (res * (10**len(str(i))) + i) % k

print(res)

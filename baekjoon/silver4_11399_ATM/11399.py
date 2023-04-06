n = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = 0

for i in range(n):
    for j in range(i + 1):
        res += lst[j]
print(res)
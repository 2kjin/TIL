n, a, d = map(int, input().split())
lst = list(map(int, input().split()))
x = 0

for i in range(n):
    if lst[i] == a:
        x += 1
        a += d

print(x)
a = list(map(int,input().split()))
b = list(map(int,input().split()))

b.sort()
cnt = 0

i = 0
while i < a[1] and a[0] < 200:
    a[0] += b[cnt]
    cnt += 1
    i += 1

    if a[0] >= 200:
        break

print(cnt)

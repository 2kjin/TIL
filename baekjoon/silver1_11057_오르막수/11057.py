n = int(input())

up = [1] * 10

for _ in range(n-1):
    for j in range(1,10):
        up[j] += up[j-1]

print(sum(up)%10007)
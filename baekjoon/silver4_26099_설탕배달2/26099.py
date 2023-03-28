n = int(input())
ans = 0

while n % 5 != 0:
    n -= 3
    ans += 1

if n < 0:
    print("-1")
else:
    print(ans + n // 5)

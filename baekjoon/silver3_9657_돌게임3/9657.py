n = int(input())
arr = [1, 3, 4]

dp = [False] * (n + 1)

for i in range(1, n+1):
    for j in arr:
        if i == j or (i > j and not dp[i-j]):
            dp[i] = True
            break

if dp[n]:
    print("SK")
else:
    print("CY")
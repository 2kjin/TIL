import sys
sys.stdin=open("input.txt")

n = int(input())
a = list(map(int,input().split()))
x = int(input())
l, r = 0, n-1
cnt = 0
a.sort()

while l < r:
    res = a[l] + a[r]
    if res == x:
        cnt += 1
    if res < x:
        l += 1
        continue
    r -= 1

print(cnt)
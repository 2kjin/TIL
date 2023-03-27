import sys
sys.stdin = open("input.txt")

n = int(input())
lst = []
for i in range(n):
    a, b = map(int,input().split())
    lst.append([a,b])
x_lst = sorted(lst, key=lambda x:x[0])
y_lst = sorted(lst, key=lambda x:x[1])

x_mid = x_lst[n//2][0]
y_mid = y_lst[n//2][1]

ans = 0
for j in lst:
    ans += (abs(x_mid-j[0])+abs(y_mid-j[1]))
print(ans)
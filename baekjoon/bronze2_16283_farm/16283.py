import sys
sys.stdin = open("input.txt")

a, b, n, w = map(int,input().split())
cnt = 0
sheep = 0
goat = 0

for i in range(1,1000):
    if a*i + b*(n-i) == w and n-i>0:
        sheep = i
        goat = (n-i)
        cnt += 1
    
if cnt == 1:
    print(sheep, goat)
else:
    print(-1)
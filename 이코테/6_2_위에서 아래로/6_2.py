import sys
sys.stdin = open("input.txt")

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
# num = list(int(input()) for _ in range(N))

lst.sort(reverse=True)
print(*lst)
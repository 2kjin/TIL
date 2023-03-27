import sys
sys.stdin = open("input.txt")

# N, M = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# res = a + b
# res.sort()

# print(*res)

N = input()

a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = a + b
res.sort()

print(' '.join(map(str,res)))
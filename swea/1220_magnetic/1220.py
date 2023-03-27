import sys
sys.stdin = open("input.txt")

for t in range(10):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            if arr[j][i] == 1:

    print(arr)
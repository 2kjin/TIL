import sys
sys.stdin = open('13755input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    result = []

    arr = []
    for i in range(N):
        arr.append(input())

        print(arr)
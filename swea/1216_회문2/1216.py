import sys
sys.stdin = open('13755input.txt')

for t in range(1, 11):
    a = int(input())
    arr = [list(map(str, input())) for _ in range(100)

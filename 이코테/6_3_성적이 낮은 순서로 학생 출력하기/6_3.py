import sys
sys.stdin= open("input.txt",'rt', encoding='UTF8')

n = int(input())
lst = []

for i in range(n):
    a = input().split()
    lst.append((a[0], int(a[1])))

lst.sort(key=lambda x:x[1])

for i in lst:
    print(i[0], end=' ')
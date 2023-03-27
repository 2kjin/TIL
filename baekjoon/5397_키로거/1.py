import sys
from collections import deque

sys.stdin = open("input.txt")

n = int(input())

# 리스트
for _ in range(n):
    password = input().rstrip()
    l, r = [], []

    for i in password:
        if i == '-':
            if l:
                l.pop()
        elif i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                r = r[::-1]
                l.append(r.pop())
                r = r[::-1]
        else:
            l.append(i)

    l = l + r[::-1]

    print(''.join(l))


## 큐
# for _ in range(n):
#     password = input()
#     l = []
#     r = deque()

#     for i in password:
#         if i == '-':
#             if l:
#                 l.pop()
#         elif i == '<':
#             if l:
#                 r.append(l.pop())
#         elif i == '>':
#             if r:
#                 l.append(r.popleft())
#         else:
#             l.append(i)

#     if r:
#         r.rotate()
#         l = l + r

#     print(''.join(l))
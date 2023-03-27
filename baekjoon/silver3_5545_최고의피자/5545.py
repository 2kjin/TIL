import sys
sys.stdin = open("input.txt")

N = int(input())                      # N : 토핑의 종류의 수
A, B = map(int,input().split())       # A : 도우가격 , B : 토핑가격
C = int(input())                      # C : 도우 열량
Dlst = []                             # D : 토핑의 열량들

for _ in range(N):
    D = int(input())
    Dlst.append(D)

Dlst.sort(reverse=True)
# 피자가격 p = A + B*N
# 피자열량 cal = C + sum(Dlst)
# res = cal / p
ans = C / A

for i in range(1,N+1):
    cal = C + sum(Dlst[0:i])
    p = A + B*i
    res = cal / p

    if res > ans:
        ans = res
    else:
        pass

print(int(ans))
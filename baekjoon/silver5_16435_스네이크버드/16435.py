import sys
sys.stdin = open("input.txt")

N, L = map(int,input().split())
H = list(map(int,input().split()))
H.sort()

for i in H:
    if i > L:
        break
    else:
        L +=1
print(L)
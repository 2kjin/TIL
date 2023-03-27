import sys
sys.stdin = open("input.txt")

# n = int(input())
# lst = []
# res = 0
# time = [[]*1001]

# for _ in range(n):
#     a, b = map(int,input().split())
#     lst.append([a,b])

# for i in range(n):
#     lst.remove(lst[i][0],lst[i][1])


#     print(lst)

n = int(input())
lst = []
time = [0] * 1001

for i in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

same = lst[::]
res = 0

for i in range(n):
    lst.pop(i)
    cnt = 0
    for j in range(n-1):
        for k in range(lst[j][0],lst[j][1]):
            if time[k] == 0:
                time[k] += 1
                cnt += 1
            else:
                pass
    time = [0] * 1001
    lst = same[::]
    if cnt > res:
        res = cnt
print(res)
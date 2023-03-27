from itertools import permutations
import sys
sys.stdin = open("input.txt")

n = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(n):
    q, s, b = map(int, input().split())
    q = list(str(q))
    cnt = 0

    for i in range(len(num)):
        s_cnt = 0
        b_cnt = 0
        i -= cnt

        for j in range(3):
            if num[i][j] == q[j]:
                s_cnt += 1
            elif q[j] in num[i]:
                b_cnt += 1
    
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            cnt += 1

print(len(num))
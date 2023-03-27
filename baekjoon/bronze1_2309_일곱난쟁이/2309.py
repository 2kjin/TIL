import sys
sys.stdin = open("input.txt")

n = 9
a, b = 0, 0
arr = list(int(input()) for _ in range(n))
result = 0
for k in arr:
    result += k                                  # arr의 총합

for i in range(n):
    for j in range(i+1, n):                      # 두개씩 묶어서 돌려라
        if result - (arr[i] + arr[j]) == 100:    # arr 총합에서 두명의 난쟁이 뺸 값이 100일때
            arr[i] = a                           # a 와 b 에 값 할당
            arr[j] = b

arr.remove(a)                                    # remove로 a,b 제거
arr.remove(b)

# 버블 정렬
for j in range(6,0,-1):
    for k in range(0,j):
        if arr[k] > arr[k+1]:
            arr[k], arr[k+1] = arr[k+1], arr[k]

# 한줄씩 출력
for l in arr:
    print(l)
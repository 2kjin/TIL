import sys
sys.stdin= open("input2.txt")
# input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
pre = arr[0]                          # 이전값 할당
max_cnt, min_cnt = 1, 1               # 이전수 보다 큰경우, 작은경우 카운트
res = 1                               # 큰 값 저장

for i in arr[1:]:                     # 위에서 이전값 할당했으니 arr[1]부터 시작
    if i >= pre:                      # 이전값 보다 크다면
        max_cnt += 1                  # 큰경우에 1씩 추가
    else:
        max_cnt = 1                   # 아니라면 초기화
    if i <= pre:                      # 이전값 보다 작다면
        min_cnt += 1                  # 작은경우에 1씩 추가
    else:
        min_cnt = 1                   # 아니라면 초기화
    pre = i                           # 이전값 i로 할당
    res = max(res, max_cnt, min_cnt)  # 큰 값 저장 후 반복
print(res)
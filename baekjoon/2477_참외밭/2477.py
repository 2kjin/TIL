import sys
sys.stdin = open("input.txt")
# input = sys.stdin.readline

n = int(input())                            # 참외 갯수
h = []
w = []
t = []
for i in range(6):
    way, cm = map(int,input().split())
    if way == 1 or way == 2:                # 동서 / 남북으로 나눠서 리스트에 넣어주기
        w.append(cm)
        t.append(cm)
    else:
        h.append(cm)
        t.append(cm)
b_b = max(h) * max(w)                       # 큰 사각형

max_h = t.index(max(h))                     # 세로 최대값 인덱스 구하기
max_w = t.index(max(w))                     # 가로 최대값 인덱스 구하기

# 세로 최대값의 인덱스 앞뒤값을 빼준 절대값 = 빈 사각형 가로값
s_w = abs(t[max_h -1] - t[max_h-5 if max_h == 5 else max_h +1])
s_h = abs(t[max_w -1] - t[max_w-5 if max_w == 5 else max_w +1])        # 같은 원리
s_b = s_w * s_h                             # 작은 사각형
res = b_b - s_b                             # 참외밭
print(res * n)
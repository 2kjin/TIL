n = 5
snail = [[0]*n for _ in range(n)]

num = 1 #0

    # 우 하 좌 상
    # 0  1  2  3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x, y = 0, -1
for num in range(1,n**2+1):
# while num <= n**2: # if ~:
            #break
    # 이동
    nx = x + dx[d]
    ny = y + dy[d]
    if 0<= nx<n and 0<=ny<n and snail[nx][ny] == 0: # 이동을 할 수 있다면
    # 숫자 넣기
        snail[x][y] = num                           # 숫자를 넣고
        x = nx                                      # 이동시켜줘
        y = ny
        # num += 1                                  # 그리고 색칠
    else:
        d = (d+1)%4
        nx = x + dx[d]                              # 바뀐 방향으로 한번 더 가줘
        ny = y + dy[d]
        # 다시 숫자 넣기
        snail[x][y] = num
        x = nx
        y = ny

from pprint import pp, pprint
pprint(snail)
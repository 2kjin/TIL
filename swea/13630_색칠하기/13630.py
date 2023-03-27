T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    box = [[0] * 10 for _ in range(10)]
 
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
 
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1:
                    box[i][j] += 1
                elif color == 2:
                    box[i][j] += 2
 
    cnt = 0
    for x in range(10):
        for y in range(10):
            if box[x][y] >= 3:
                cnt += 1
 
    print(f'#{t} {cnt}')
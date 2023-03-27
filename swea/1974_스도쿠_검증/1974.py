import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        row_s = 0
        col_s = 0
        for j in range(9):
            row_s += N[i][j]
            col_s += N[j][i]
        if row_s == 45 and col_s == 45:
            result = result * 1
        else:
            result = result * 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_s = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    box_s += N[k][l]
            if box_s == 45:
                result = result * 1
            else:
                result = result * 0
                break

    print(f'#{t} {result}')









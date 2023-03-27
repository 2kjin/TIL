code_dic = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
 
    def solve():
        global lst
        for i in range(N):
            for j in range(M - 1, 54, -1):
                if data[i][j] == 1:
                    r, c = i, j
                    for i in range(8):
                        n1 = n2 = n3 = n4 = 0
                        while data[r][c] == 1:
                            n4 += 1
                            c -= 1
                        while data[r][c] == 0:
                            n3 += 1
                            c -= 1
                        while data[r][c] == 1:
                            n2 += 1
                            c -= 1
                        n1 = 7 - n2 - n3 - n4
                        c -= n1
                        lst.append(code_dic[(n1, n2, n3, n4)])
                    return lst
 
    lst = []
    solve()
     
    if ((lst[1] + lst[3] + lst[5] + lst[7]) * 3 + (lst[0] + lst[2] + lst[4] + lst[6])) % 10 == 0:
        print(f"#{tc} {sum(lst)}")
    else:
        print(f"#{tc} 0")
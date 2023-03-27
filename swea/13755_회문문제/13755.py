T = int(input())
 
for t in range(1, T+1):
    a, b = map(int, input().split())
    arr = [list(input()) for _ in range(a)]
    arr_reverse = [[arr[j][i] for j in range(a)] for i in range(a)]
    result = []
 
    #가로 검색
    for r in range(a):
        for c in range(a - b + 1):
            if arr[r][c : c + b] == arr[r][c : c + b][ : : -1]:
                print(f'#{t}', ''.join(arr[r][c: c + b]))
 
    #세로 검색
    for r in range(a):
        for c in range(a - b + 1):
            if arr_reverse[r][c: c + b] == arr_reverse[r][c: c + b][::-1]:
                print(f'#{t}', ''.join(arr_reverse[r][c: c + b]))
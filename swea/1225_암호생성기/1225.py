import sys
sys.stdin = open("input.txt")

for t in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))
    flag = 0

    while code:
        for i in range(1, 6):
            n = code.pop(0)
            if n - i <= 0:
                code.append(0)
                flag = 1
                break
            code.append(n - i)
        if flag ==1 :
            break

    print(f'#{t}', *code)
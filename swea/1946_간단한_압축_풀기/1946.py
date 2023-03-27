import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    result = ''
    for i in range(n):
        n, cnt = input().split()
        cnt = int(cnt)
        result += n * cnt

    print(f'#{t} {result}')
    # for i in range(len(result)):
    #     if (i+1)%10 == 0:
    #         print(result[i])
    #     else:
    #         print(result[i], end='')
    # print()
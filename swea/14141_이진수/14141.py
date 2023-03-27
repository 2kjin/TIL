def bi(n):
    b = ''
    for j in range(4):
        a = n % 2
        n = n // 2
        b = str(a) + b
    return b
  
  
T = int(input())
for tc in range(T):
  
    N, M = input().split()
    res = ''
  
    for i in M:
        if not i.isdigit():
            res = res + bi(ord(i) - 55)
        else:
            res = res + bi(int(i))
    print(f'#{tc + 1} {res}')
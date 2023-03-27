T = int(input())
for t in range(1, T + 1):
    a, b = input().split()
    c = len(a.replace(b, '1'))
 
    print(f'#{t} {c}')
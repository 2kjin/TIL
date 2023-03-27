T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    nums = [2, 3, 5, 7, 11]
    cnt = [0, 0, 0, 0, 0]
    for i in range(5):
        while N % nums[i] == 0:
            N = N // nums[i]
            cnt[i] += 1
    print(f'#{t} ', end='')
    print(*cnt)
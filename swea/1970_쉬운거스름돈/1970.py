import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    nums = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    pay = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(nums)):
        while N % nums[i] == 0:
            N = N // nums[i]
            pay[i] += 1

    print(f'#{t} ',end='')
    print(*pay)

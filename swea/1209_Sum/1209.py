for _ in range(10) :
    T = int(input())
 
    nums = []
    for i in range(100) :
        nums.append(list(map(int, input().split())))
 
    max_1 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += nums[i][j]
        if sum > max_1 :
            max_1 = sum
 
    max_2 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += nums[j][i]
        if sum > max_2 :
            max_2 = sum
 
    max_3 = 0
    for i in range(100) :
        sum1 = 0 ; sum2 = 0
        sum1 += nums[i][i]
        sum2 += nums[i][99-i]
    if max(sum1, sum2) > max_3 :
        max_3 = max(sum1, sum2)
 
    print(f'#{T} {max(max_1, max_2, max_3)}')
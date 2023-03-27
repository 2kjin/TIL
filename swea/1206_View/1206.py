for t in range(1,11):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    for num in range(1,256):
        zero_arr = [0] * N
        for i in range(0, N-2):
            if arr[i] >= num:
                zero_arr[i] += num
        for j in range(2, N-2):
            if zero_arr[j] > 0 and zero_arr[j-2] + zero_arr[j-1] + zero_arr[j+1] + zero_arr[j+2] == 0:
                cnt += 1
    print(f"#{t} {cnt}")
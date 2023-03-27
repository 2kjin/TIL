T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
 
    for i in range(10):
        if i%2 ==0:
            max_idx = i
            for j in range(i+1,N):
                if lst[j] > lst[max_idx]:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
 
        else:
            min_idx = i
            for j in range(i+1,N):
                if lst[j] < lst[min_idx]:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
 
    print(f'#{tc}',*lst[:10])
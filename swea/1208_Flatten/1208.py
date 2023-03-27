for t in range(10) :
    N = int(input())
    box = list(map(int, input().split()))
 
    for i in range(N) :
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1
        box[min_index] += 1
 
    print(f'#{t+1} {max(box)-min(box)}')
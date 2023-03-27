import sys
sys.stdin = open("input.txt")

n = int(input())
card = list(map(int,input().split()))
m = int(input())
lst = list(map(int,input().split()))
card.sort()

for i in lst:
    l = 0
    r = n-1
    res = False

    while l <= r:
        mid = ( l + r ) // 2
        if card[mid] > i:
            r = mid - 1
        elif card[mid] < i:
            l = mid + 1
        else:
            res = True
            break
        
    if res:
        print(1, end=' ')
    else:
        print(0, end=' ')



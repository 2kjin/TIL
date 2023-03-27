import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1,T+1):
    P, A, B = map(int,input().split())

    start = 0
    end = P
    middle = int((l+r)/2)

    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    # def serch(a, n, key)
    #     start = 0
    #     end = N-1
    #     while start <= end:
    #         middle = (start + end) //2
    #         if a[middle] == key
    #             return true
    #         elif a[middle] > key:
    #             end = middle -1
    #         else:
    #             start = middle + 1
    #     return false



    print(f'#{t} {P} {A} {B}')
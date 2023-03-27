T = int(input())
 
for t in range(1,T+1):
    a, b = map(int,input().split())
    a_lst = list(map(int,input().split()))
    b_lst = list(map(int,input().split()))
    res = 0
 
    if a < b :
        for i in range(b-a+1):
            lst_sum = 0
            for j in range(a):
                lst_sum += a_lst[j] * b_lst[i+j]
            if res < lst_sum:
                res = lst_sum
    else:
        for i in range(a-b+1):
            lst_sum = 0
            for j in range(b):
                lst_sum += a_lst[i+j] * b_lst[j]
            if res < lst_sum:
                res = lst_sum
 
    print(f'#{t} {res}')
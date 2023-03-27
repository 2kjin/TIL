for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
     
    print(f'#{t+1} {max(lst)-min(lst)}')
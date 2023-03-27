for test in range(int(input())):
    card=int(input())
    lst=list(map(str,input()))
    cnt=[0]*10
 
    for i in range(card):
        cnt[int(lst[i])]+=1
     
    result=0
    for i in range(len(cnt)):
        if result<=cnt[i]:
            result=cnt[i]
            idx=i
 
    print(f'#{test+1} {idx} {result}')
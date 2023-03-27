T = int(input())
for t in range(1, T+1):
    a = input()
    lst=[]
 
    for i in a:
        if lst and i == lst[-1]:
            lst.pop()
        else:
            lst.append(i)
    b = len(lst)
     
    print(f'#{t} {b}')
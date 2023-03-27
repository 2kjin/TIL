T = int(input())
 
for t in range(1,T+1):
    card = input()
    lst = []
    card_lst = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
 
    for i in range(0, len(card), 3):
        lst.append(card[i:i+3])
 
    if len(lst) != len(set(lst)):
        print(f'#{t} ERROR')
    else:        
        for i in range(0, len(card)-2, 3):
            num = card_lst[card[i]] - 1
            card_lst[card[i]] = num
 
        print(f'#{t}', end=' ')
        print(*card_lst.values())
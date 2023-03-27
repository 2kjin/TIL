T = int(input())
 
def check(p):
    for j in range(10):
        if p[j] == 3:
            return True
    for k in range(8):
        if p[k] and p[k + 1] and p[k + 2]:
            return True
    return False
 
for t in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    win = 0
 
    for i in range(12):
        if i % 2 == 0:
            p1[card[i]] += 1
            if check(p1):
                win = 1
                break
        else:
            p2[card[i]] += 1
            if check(p2):
                win = 2
                break
 
    print(f"#{t} {win}")T = int(input())
 
def check(p):
    for j in range(10):
        if p[j] == 3:
            return True
    for k in range(8):
        if p[k] and p[k + 1] and p[k + 2]:
            return True
    return False
 
for t in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    win = 0
 
    for i in range(12):
        if i % 2 == 0:
            p1[card[i]] += 1
            if check(p1):
                win = 1
                break
        else:
            p2[card[i]] += 1
            if check(p2):
                win = 2
                break
 
    print(f"#{t} {win}")
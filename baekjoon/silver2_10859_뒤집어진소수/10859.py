import sys
sys.stdin = open("input.txt")

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False # 소수아님
    return True # 소수

N = input()
n_ans = int(N)
n = N[::-1]
lst=list(map(str, n))
res = "yes"

if '3' in lst or '4' in lst or '7' in lst:
    res = "no"
else:
    if isPrime(n_ans):
        for i in range(len(lst)):
            if lst[i] == '6':
                lst[i] = '9'
            elif lst[i] == '9':
                lst[i] = '6'
        ans = int("".join(lst))
        if isPrime(ans):
            pass
        else:
            res = "no"
    else:
        res = "no"
print(res)
import sys
sys.stdin = open("input.txt")

a,b,d = map(int, input().split())
def prime_list(a,b):
    sieve = [True] * b

    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i] == True: 
            for j in range(i+i, b, i):
                sieve[j] = False

    return [i for i in range(a, b) if sieve[i] == True]
lst = prime_list(a,b)
cnt = 0
for n in lst:
    if str(d) in str(n):
        cnt += 1
print(cnt)
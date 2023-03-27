import sys
sys.stdin = open('GNS_test_input.txt')

num_alpha = ['ZRO','ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for case in range(1, T+1):
    n, m = list(map(str,input().split()))
    m = int(m)
    num_lst = list(map(str,input().split()))
    ans = []

    for i in range(10):
        for k in num_lst:
            if num_alpha[i] == k:
                ans.append(k)

    print(n)
    print(*ans)
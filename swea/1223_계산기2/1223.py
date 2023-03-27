for t in range(1, 11):
    N = int(input())
    infix = input()
    S = []                                                              # push: List.append(), pop: List.pop()
    postfix = ''
    for token in infix:
        if token in '+*':
            while S and token == '+' and S[-1] == '*':      # token 과 S[top]과 우선순위 비교
                postfix += S.pop()
            S.append(token)
        else:
            postfix += token
 
    while S:
        postfix += S.pop()
         
    for token in postfix:                                           # 후위 표기 계산하기
        if token in '+*':
            b = S.pop()
            a = S.pop()
            if token == '+': S.append(a + b)
            else: S.append(a * b)
        else:
            S.append(int(token))
 
    print(f'#{t} {S[0]}')
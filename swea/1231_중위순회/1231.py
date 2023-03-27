def inorder(a):
    if a <= N:
        inorder(a * 2)
        print(tree[a],end='')
        inorder(a * 2 + 1)
  
for t in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        lst = list(input().split())
        tree[i + 1] = lst[1]
    print(f'#{t}', end=' ')
    inorder(1)
    print()
def maketree (s, e, k):
    if s <= e:
        mid = (s+e)//2
        tree[k].append(arr[mid])

        maketree(s, mid-1, k+1)
        maketree(mid+1, e, k+1)

K = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(K)]
maketree(0, len(arr)-1, 0)

for t in tree:
    print(*t)
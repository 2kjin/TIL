import sys
k = int(sys.stdin.readline())
lst = list(map(str, sys.stdin.readline().split()))
visited = [False] * 10
mx, mn = "", ""

def poss(i, j, l):
    if l == ">":
        return i > j
    else:
        return i < j
def backTracking(idx, word):
    global mx, mn
    if idx > k:
        if len(mn) == 0:
            mn = word
        else:
            mx = word
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0 or poss(word[-1], str(i), lst[idx - 1]):
                visited[i] = True
                backTracking(idx + 1, word + str(i))
                visited[i] = False

backTracking(0, "")

print(mx)
print(mn)
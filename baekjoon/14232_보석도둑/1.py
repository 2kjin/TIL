import sys
sys.stdin = open("input.txt")

k = int(input())
arr = []

for i in range(2,k):
    if i*i > k:
        break
    while k % i == 0:
        arr.append(i)
        k //= i
if k != 1:
    arr.append(k)

print(len(arr))
print(*arr)

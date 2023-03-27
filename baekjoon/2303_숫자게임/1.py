n = int(input())
lst = []
for _ in range(n):
  card = list(map(int, input().split()))
  res_max = 0
  for i in range(5):
    for j in range(i + 1, 5):
      for k in range(j + 1, 5):
        res = (card[i] + card[j] + card[k]) % 10
        if res >= res_max:
          res_max = res
  lst.append(res_max)

for i in range(n - 1, -1, -1):
  if lst[i] == max(lst):
    print(i + 1)
    break
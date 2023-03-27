import sys
sys.stdin = open("sample_input.txt")

from collections import deque
  
T = int(input())
  
for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    for m in range(M):
        queue.append(queue.popleft())
  
    print(f'#{t} {queue[0]}')
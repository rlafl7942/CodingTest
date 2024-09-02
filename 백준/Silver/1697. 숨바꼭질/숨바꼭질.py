import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [0] * 100001

while q:
  tmp = q.popleft()

  if tmp == k:
    print(visited[tmp])
    break

  for i in (tmp-1, tmp+1, tmp*2):
    if 0<=i<=100000 and visited[i] == 0:
      visited[i] = visited[tmp] + 1
      q.append(i)

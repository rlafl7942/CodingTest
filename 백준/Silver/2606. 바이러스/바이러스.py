import sys
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  cnt = 0
  if not visited[v]:
    visited[v] = True
  
  q = deque()
  q.append(v)

  while q:
    tmp = q.popleft()

    for i in graph[tmp]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        cnt+=1

  return cnt

print(bfs(1))
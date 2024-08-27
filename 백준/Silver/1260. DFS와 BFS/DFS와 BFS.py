import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

visited_bfs[0] = True
visited_dfs[0] = True

def dfs(x):
  visited_dfs[x] = True
  print(x, end=" ")
  for i in graph[x]:
    if visited_dfs[i] == False:
      dfs(i)

def bfs(x):
  q = deque([x])
  visited_bfs[x] = True
  while q:
    X = q.popleft()
    print(X, end=" ")
    for i in graph[X]:
      if visited_bfs[i] == False:
        q.append(i)
        visited_bfs[i] = True

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

dfs(v)
print()
bfs(v)
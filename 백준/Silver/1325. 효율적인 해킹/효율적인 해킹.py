import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

def bfs(v):
  q = deque([v])
  length = 0
  visited = [False] * (n+1)
  visited[v] = True
  while q:
    x = q.popleft()
    for i in graph[x]:
      if visited[i] == False:
        length+=1
        q.append(i)
        visited[i] = True
  return length

result = []
for i in range(1, len(graph)):
  result.append(bfs(i))

maxL = max(result)
for i in range(0, len(result)):
  if result[i] == maxL:
    print(i+1, end=" ")
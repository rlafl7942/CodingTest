import sys
from collections import deque

input = sys.stdin.readline
graph = []

n,m = map(int, input().split())

for i in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
  q = deque()
  q.append((x,y))

  while q:
    a, b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[a][b] + 1
        q.append((nx,ny))
    
bfs(0,0)
print(graph[n-1][m-1])
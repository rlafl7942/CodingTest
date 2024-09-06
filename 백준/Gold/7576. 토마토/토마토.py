import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
q = deque()
for _ in range(m):
  tomato = list(map(int, input().split()))
  graph.append(tomato)

for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      q.append((i, j))

def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx>=0 and nx<m and ny>=0 and ny<n:
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          q.append((nx, ny))

bfs()

answer = 0
for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      print(-1)
      exit()
    else:
      answer = max(answer, graph[i][j])

print(answer-1)
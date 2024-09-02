import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  cnt = 1

  while q:
    a, b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 1:
        cnt+=1
        graph[nx][ny] = 0
        q.append((nx, ny))

  return cnt

for _ in range(t):
  n, m, k = map(int, input().split())
  graph = [[0 for _ in range(m)] for _ in range(n)]
  answer = []
  for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        answer.append(bfs(i,j))
  print(len(answer))
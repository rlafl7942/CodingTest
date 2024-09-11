import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
q = deque()
for _ in range(h):
  tmp = []
  for _ in range(n):
    tomato = list(map(int, input().split()))
    tmp.append(tomato)
  graph.append(tmp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        q.append((i, j, k))

while q:
  z, y, x = q.popleft()
  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]

    if nx>=0 and nx<m and ny>=0 and ny<n and nz>=0 and nz<h:
      if graph[nz][ny][nx] == 0:
        graph[nz][ny][nx] = graph[z][y][x] + 1
        q.append((nz, ny, nx))

tmp = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0:
        print(-1)
        exit()
      if tmp < graph[i][j][k]:
        tmp = graph[i][j][k]

print(tmp-1)
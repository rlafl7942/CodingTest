import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split()) # 5 7 3
graph = [[1 for _ in range(m)] for _ in range(n)]
q = deque()

for _ in range(k):
  lx, ly, rx, ry = map(int, input().split()) # 0 2 4 4
  for i in range(ly, ry):
    for j in range(lx, rx):
      graph[i][j] = -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i, j))
      graph[i][j] = 0
      cnt = 1
      while q:
        x, y = q.popleft()
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]

          if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny] == 1:
              cnt+=1
              graph[nx][ny] = 0
              q.append((nx, ny))
      answer.append(cnt)

print(len(answer))
answer.sort()
for i in range(len(answer)):
  print(answer[i], end=" ")
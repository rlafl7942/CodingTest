import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i, j):
  q = deque()
  q.append((i,j))
  cnt = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx>=0 and nx<n and ny>=0 and ny<m:
        if farm[nx][ny] == 1:
          farm[nx][ny] += 1
          q.append((nx, ny))
          cnt+=1

  return cnt


t = int(input())
for _ in range(t):
  n, m, k = map(int, input().split())
  farm = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    farm[x][y] = 1

  answer = []
  for i in range(n):
    for j in range(m):
      if farm[i][j] == 1:
        answer.append(BFS(i, j))
  
  print(len(answer))

import sys
from collections import deque

n = int(input())
graph=[]
answer=[]

for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  graph[x][y] = 0
  cnt=1

  while q:
    a,b = q.popleft()
    
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx, ny))
        cnt+=1

  answer.append(cnt)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i,j)

answer.sort()
print(len(answer))
for i in answer:
  print(i)
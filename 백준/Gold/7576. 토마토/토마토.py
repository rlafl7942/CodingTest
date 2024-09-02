import sys
from collections import deque

input = sys.stdin.readline


queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      queue.append([i,j]) # 익은 토마토 먼저 queue에 넣어주기

while queue:
  x,y = queue.popleft() # 하나씩 빼서 확인
  for i in range(4): # 상하좌우 확인
    nx, ny = dx[i]+x, dy[i]+y
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y]+1 # 날짜수 더해주기
        queue.append([nx,ny]) # 익었으니까 queue에 넣어주기

ans = 0
for i in tomato:
  for j in i:
    if j == 0: # 안익은거 있으면 -1
      print(-1)
      exit()

  ans = max(ans, max(i)) 

print(ans - 1)

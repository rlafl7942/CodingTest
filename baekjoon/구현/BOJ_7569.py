import sys
from collections import deque

input = sys.stdin.readline


queue = deque()
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
m, n, o = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(o)]

for i in range(o):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k] == 1:
        queue.append([i,j,k])


while queue:
  x,y,z = queue.popleft() # 하나씩 빼서 확인
  for i in range(6): 
    nx, ny, nz = dx[i]+x, dy[i]+y, dz[i]+z
    if nx>=0 and nx<o and ny>=0 and ny<n and nz>=0 and nz<m:
      if tomato[nx][ny][nz] == 0:
        tomato[nx][ny][nz] = tomato[x][y][z]+1 # 날짜수 더해주기
        queue.append([nx,ny,nz]) # 익었으니까 queue에 넣어주기

ans = 0

for i in tomato:
  for j in i:
    if 0 in j:
      print(-1)
      exit()
    ans = max(ans, max(j)) 

print(ans - 1)

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
i = 0
j = 0

limit = min(n,m) // 2 # n,m 중에 작은 값 기준 //2

for _ in range(r):
  for i in range(limit):
    x, y = i, i
    tmp_current = arr[x][y]
  # 각각 경우 나눠서 진행
    for j in range(i+1, n-i): # 아래쪽 방향
      x = j
      tmp_next = arr[x][y]
      arr[x][y] = tmp_current
      tmp_current = tmp_next

    for j in range(i+1, m-i): # 오른쪽 방향
      y = j
      tmp_next = arr[x][y]
      arr[x][y] = tmp_current
      tmp_current = tmp_next
    
    for j in range(i+1, n-i): # 위쪽 방향
      x = n-j-1
      tmp_next = arr[x][y]
      arr[x][y] = tmp_current
      tmp_current = tmp_next

    for j in range(i+1, m-i): # 왼쪽 방향
      y = m-j-1
      tmp_next = arr[x][y]
      arr[x][y] = tmp_current
      tmp_current = tmp_next

for i in range(n):
  for j in range(m):
    print(arr[i][j], end=" ")
  print()
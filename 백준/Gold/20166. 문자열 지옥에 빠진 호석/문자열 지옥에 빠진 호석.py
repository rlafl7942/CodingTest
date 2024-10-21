from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = []
god = []
ans = defaultdict(int)
q = deque()
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for _ in range(n):
  graph.append(list(input().strip()))

for _ in range(k):
  word = input().strip()
  god.append(word)
  ans[word] = 0

# def dfs(a, b, string):
  
#   if len(string) > 5:
#     return

#   if string in ans:
#     ans[string] += 1
  
#   for i in range(8):
#     nx = (n + a + dx[i]) % n
#     ny = (m + b + dy[i]) % m

#     dfs(nx, ny, string + graph[nx][ny])

def dfs(a, b, string):
  q.append((a, b, string))
  
  while q:
    x, y, word = q.popleft()

    if len(word) > 5:
      continue

    if word in ans:
      ans[word] += 1

    for i in range(8):
      nx = (x+dx[i])%n
      ny = (y+dy[i])%m

      q.append((nx, ny, word + graph[nx][ny]))

for i in range(n):
  for j in range(m):
    dfs(i, j, graph[i][j])

for i in god:
  print(ans[i])
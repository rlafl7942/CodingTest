import sys

input = sys.stdin.readline

def dfs(x):
  global cnt
  visited[x] = True
  for i in connected[x]:
    if not visited[i]:
      cnt+=1
      dfs(i)

cnt = 0
n = int(input())
connected = [[] for _ in range(n+1)]
visited = [False] * (n+1)

computer = int(input())
for _ in range(computer):
  a,b = map(int, input().split())
  connected[a].append(b)
  connected[b].append(a)

dfs(1)

print(cnt)

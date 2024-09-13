import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1] * 100001

def bfs():
  visited[n] = 0
  q = deque([n])

  while q:
    now = q.popleft()

    if now == k:
      return visited[now]

    for next in (now-1, now+1, now*2):
      if next>=0 and next<=100000 and visited[next] == -1:
        if next == now*2:
          visited[next] = visited[now]
          q.appendleft(next)
        else:
          visited[next] = visited[now] + 1
          q.append(next)

print(bfs())
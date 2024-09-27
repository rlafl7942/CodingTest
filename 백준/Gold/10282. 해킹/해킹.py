import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))

  total = [sys.maxsize] * (n+1)
  total[c] = 0
  visited = [False] * (n+1)
  visited[c] = True
  q = []
  heapq.heappush(q, (c, 0))

  while q:
    computer, time = heapq.heappop(q)

    if total[computer] < time:
      continue

    for ncomputer, ntime in graph[computer]:
      if total[ncomputer] > ntime + time:
        total[ncomputer] = ntime + time
        heapq.heappush(q, (ncomputer, ntime+time))
        visited[ncomputer] = True

  sum = 0
  max = 0
  for i in range(len(visited)):
    if visited[i]:
      sum+=1
      if total[i] > max:
        max = total[i]
  print(sum, max)
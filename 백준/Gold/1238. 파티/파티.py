import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  start, end, time = map(int, input().split())
  graph[start].append((end, time))

def dijkstra(x, y):
  total = [sys.maxsize] * (n+1)
  total[x] = 0
  q = []
  heapq.heappush(q, (0, x))

  while q:
    cost, node = heapq.heappop(q)

    if node == y:
      return total[node]

    if total[node] < cost:
      continue

    for nnode, ncost in graph[node]:
      if total[nnode] > ncost + cost:
        total[nnode] = ncost + cost
        heapq.heappush(q, (ncost + cost, nnode))

answer = 0
for i in range(n):
  go = dijkstra(i+1, x)
  back = dijkstra(x, i+1)
  answer = max(answer, go+back)

print(answer)
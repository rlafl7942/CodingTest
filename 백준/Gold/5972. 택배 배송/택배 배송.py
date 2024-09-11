import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra():
  q = []
  heapq.heappush(q, (1, 0))
  total = [sys.maxsize] * (n+1)
  total[1] = 0

  while q:
    node, cost = heapq.heappop(q)
    if node == n:
      return total[node]
    if total[node] < cost:
      continue
    for nnode, ncost in graph[node]:
      if cost + ncost < total[nnode]:
        total[nnode] = cost+ncost
        heapq.heappush(q, (nnode, ncost+cost))

print(dijkstra())
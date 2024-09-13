import heapq
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]
distance = [sys.maxsize] * (d+1)

for i in range(d):
  graph[i].append((i+1, 1))

for _ in range(n):
  start, end, len = map(int, input().split())
  if end<=d:
    graph[start].append((end, len))

q = []

heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
  node, cost = heapq.heappop(q)

  for nnode, ncost in graph[node]:
    if distance[nnode] > distance[node] + ncost:
      distance[nnode] = distance[node] + ncost
      heapq.heappush(q, (nnode, distance[nnode]+ncost))

print(distance[d])
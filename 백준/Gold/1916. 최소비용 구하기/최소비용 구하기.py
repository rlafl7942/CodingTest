import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[] for _ in range(n+1)]
total = [sys.maxsize] * (n+1)

for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))

START, END = map(int, input().split())

def dijkstra():
  q = []
  heapq.heappush(q, (START, 0))
  total[START] = 0

  while q:
    node, cost = heapq.heappop(q)
    if cost > total[node]:
      continue

    for nnode, ncost in graph[node]:
      if total[nnode] > total[node] + ncost:
        total[nnode] = total[node] + ncost
        heapq.heappush(q, (nnode, total[node]+ncost))

dijkstra()
print(total[END])
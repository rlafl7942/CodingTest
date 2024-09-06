import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
answer = 0

for _ in range(n):
  graph.append(list(map(int, input().split())))

empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j]==0]

for combi in combinations(empty, 3): # empty 중에 3개 고르기
  new_graph = copy.deepcopy(graph) # 기존 그래프에 영향 없이 복사하기
  for i, j in combi:
    new_graph[i][j] = 1 # 벽 세우기
  
  virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

  while virus:
    x, y = virus.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if new_graph[nx][ny] == 0:
          new_graph[nx][ny] = 2
          virus.append((nx, ny)) # 바이러스 퍼뜨리기

  cnt = 0
  for row in new_graph:
    cnt += row.count(0) # 살아남은 공간 개수 세기
  answer = max(answer, cnt)
print(answer)
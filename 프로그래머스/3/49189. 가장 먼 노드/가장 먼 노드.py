from collections import deque
import sys
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [sys.maxsize] * (n+1)
    
    for value in edge:
        a, b = value[0], value[1]
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append((1, 0))
    distance[1] = 0
    distance[0] = 0
    
    while q:
        node, dist = q.popleft()
        
        for i in graph[node]:
            if distance[i] == sys.maxsize:
                distance[i] = distance[node] + 1
                q.append((i, distance[node]+1))
    
    max_dist = max(distance)
    for index, value in enumerate(distance):
        if value == max_dist:
            answer += 1
    return answer
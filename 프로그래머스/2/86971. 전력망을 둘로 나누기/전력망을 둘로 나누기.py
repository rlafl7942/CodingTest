from collections import deque
def dfs(graph, v):
    visited = [v]
    q = deque()
    q.append(v)
    cnt = 1
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                q.append(i)
                cnt += 1
    
    return cnt

def solution(n, wires):
    answer = []
    
    for i in range(len(wires)):
        st_a, st_b = wires[i][0], wires[i][1]
        graph = [[] for _ in range(n+1)]
        for wire in wires:
            if wires[i] != wire:
                a, b = wire[0], wire[1]
                graph[a].append(b)
                graph[b].append(a)
        
        tmp_1 = dfs(graph, st_a)
        tmp_2 = dfs(graph, st_b)
        
        answer.append(abs(tmp_1 - tmp_2))
        
    return min(answer)
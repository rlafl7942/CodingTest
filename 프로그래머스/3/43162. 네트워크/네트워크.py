from collections import deque
def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * (n)
    q = deque()
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i!=j:
                if computers[i][j] == 1:
                    graph[i].append(j)
                
    def bfs(v):
        q.append(v)
        cnt=0
        if not visited[v]:
            visited[v] = True
            
        while q:
            tmp = q.popleft()
            for i in graph[tmp]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    cnt+=1
        return cnt
    
    answer = []
    for i in range(0, n):
        answer.append(bfs(i))
        
    return n-sum(answer)
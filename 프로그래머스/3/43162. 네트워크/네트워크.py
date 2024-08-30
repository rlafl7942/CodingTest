from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    q = deque()
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i!=j:
                if computers[i][j]==1:
                    graph[i].append(j)
    
    def bfs(v):
        q.append(v)
        cnt=0
        if visited[v] == False:
            visited[v] = True
           
            while q:
                tmp = q.popleft()
                for i in graph[tmp]:
                    if not visited[i]:
                        q.append(i)
                        cnt+=1
                        visited[i] = True
        return cnt

    print(graph)
    l=[]
    for i in range(0, n):
        tmp = bfs(i)
        l.append(tmp)
    
    return n-sum(l)
            
        
        
    
def solution(n, computers):  
    def dfs(v):
        visited[v] = True
        for i in connected[v]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
    
    connected = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                connected[i].append(j)
                connected[j].append(i) 
    
    visited=[False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer +=1
    
    return answer
            
        
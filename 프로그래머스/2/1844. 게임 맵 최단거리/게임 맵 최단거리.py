from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    graph = []
    
    for i in range(n):
        graph.append(maps[i])
    
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >=0 and nx <n and ny >=0 and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                    
    if graph[n-1][m-1] == 1:
        return -1
    else:
        return graph[n-1][m-1]
    
    return answer
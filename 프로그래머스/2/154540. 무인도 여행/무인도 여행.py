import sys

sys.setrecursionlimit(10**5)

def solution(maps):
    global total
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    total = 0
    
    def dfs(x, y):
        global total
        visited[x][y] = True
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    total += int(maps[nx][ny])
                    dfs(nx, ny)
                
    for index, map in enumerate(maps):
        for i in range(len(maps[index])):
            if maps[index][i] != "X" and not visited[index][i]:
                total = int(maps[index][i])
                dfs(index, i)
                
                if total > 0:
                    answer.append(total)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
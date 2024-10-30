from collections import deque
import copy
def solution(maps): # 입구 -> 레버 + 레버 -> 출구
    answer = 0
    q = deque()
    graph = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    
    for index, value in enumerate(maps):
        tmp = []
        for i in range(len(maps[index])):
            if maps[index][i] == "S":
                start = [index, i]
                tmp.append(0)
            elif maps[index][i] == "E":
                end = [index, i]
                tmp.append(0)
            elif maps[index][i] == "L":
                l = [index, i]
                tmp.append(0)
            elif maps[index][i] == "X":
                tmp.append(1)
            else:
                tmp.append(0)
        graph.append(tmp)
        
    q.append(start)
    
    first_step = copy.deepcopy(graph)
    second_step = copy.deepcopy(graph)

    while q:
        x, y = q.popleft()
        if [x, y] == l:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >=0 and nx < n and ny >=0 and ny < m:
                if first_step[nx][ny] == 0:
                    q.append((nx, ny))
                    first_step[nx][ny] = first_step[x][y] + 1
    
    q = deque()
    q.append(l)
    if first_step[l[0]][l[1]] == 0:
        return -1
    while q:
        x, y = q.popleft()
        if [x, y] == end:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if second_step[nx][ny] == 0:
                    q.append((nx, ny))
                    second_step[nx][ny] = second_step[x][y] + 1

    if second_step[end[0]][end[1]] == 0:
        return -1
    return first_step[l[0]][l[1]] + second_step[end[0]][end[1]]
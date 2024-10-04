from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        start, routes, visited = q.popleft()
        
        if len(visited) == len(tickets):
            answer.append(routes)
        
        for index, ticket in enumerate(tickets):
            if ticket[0] == start and not index in visited:
                q.append((ticket[1], routes+[ticket[1]], visited+[index]))
                
    answer.sort()
    return answer[0]
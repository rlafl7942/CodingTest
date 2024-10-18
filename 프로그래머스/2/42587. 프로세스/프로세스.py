from collections import deque
def solution(priorities, location):
    answer = 0
    max_rank = max(priorities)
    q = deque()
    for index, value in enumerate(priorities):
        q.append([index, value])
        
    cnt = 0
    while q:
        x = q.popleft()
        loc, pri = x[0], x[1]
        if pri == max(priorities):
            if loc == location:
                return cnt+1
            priorities[loc] = -1
            max_rank = max(priorities)
            cnt += 1
        else:
            q.append(x)
    
    return answer
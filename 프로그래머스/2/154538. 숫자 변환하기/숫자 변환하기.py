from collections import deque
def solution(x, y, n):
    answer = 0
    cnt = 0
    if x == y:
        return 0
    q = deque()
    q.append((y, cnt))
    
    while q:
        num, count = q.popleft()
        
        if num == x:
            answer = count
            break
        
        if num > x:
            if num % 3 == 0:
                q.append((num//3, count+1))
            if num % 2 == 0:
                q.append((num//2, count+1))
            if num - n > 0:
                q.append((num-n, count+1))
                
    if answer:
        return answer
    else:
        return -1
    return answer
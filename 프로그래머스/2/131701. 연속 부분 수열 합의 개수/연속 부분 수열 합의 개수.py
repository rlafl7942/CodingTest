from collections import deque
def solution(elements):
    answer = []
    for i in range(1, len(elements)+1):
        q = deque(maxlen = i)
        for j in elements*2:
            q.append(j)
            answer.append(sum(q))
    
    return len(set(answer))
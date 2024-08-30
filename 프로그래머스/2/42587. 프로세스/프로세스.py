from collections import deque

def solution(priorities, location):
    index = deque()
    order = []
    queue = deque(priorities)

    for i in range(len(priorities)):
        index.append(i)
    
    maxP = max(queue)
    indexCnt = 0
    while queue:
        if queue[0] >= maxP:
            queue.popleft()
            order.append(index.popleft())
            if queue:
                maxP = max(queue)
        else:
            tmp = queue.popleft()
            queue.append(tmp)
            index.append(index.popleft())
    for i in range(len(order)):
        if location == order[i]:
            return (i+1)
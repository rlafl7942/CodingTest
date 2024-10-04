from heapq import heappush, heappop
def solution(operations):
    q = []
    
    for operation in operations:
        order, num = operation.split()
        num = int(num)
        
        if order == "I":
            heappush(q, num)
        else:
            if q:
                if num == -1:
                    heappop(q)
                else:
                    q.sort()
                    q.pop()
        
    q.sort()
    if q:
        return [q[-1], q[0]]
    else:
        return [0,0]
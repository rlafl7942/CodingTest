from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0
    current = 0
    while trucks:
        current -= q.popleft()
        current += trucks[0]
        if current <= weight:
            q.append(trucks.popleft())
        else:
            current -= trucks[0]
            q.append(0)
        time+=1
        
    if q:
        return time + len(q)
    else:
        return time
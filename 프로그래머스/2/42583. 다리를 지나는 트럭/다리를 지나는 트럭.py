from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = 0
    truck_weights = deque(truck_weights)
    bridge_weight = deque([0] * bridge_length)
    
    while truck_weights:
        answer += 1
        current -= bridge_weight.popleft()
        if current + truck_weights[0] <= weight:
            current += truck_weights[0]
            bridge_weight.append(truck_weights.popleft())
            
        else:
            bridge_weight.append(0)
    
    return answer+bridge_length
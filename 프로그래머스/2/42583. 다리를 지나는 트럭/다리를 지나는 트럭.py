from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge_weight = deque([0] * bridge_length)
    current_weight = 0
    answer = 0
    while truck_weights:
        answer += 1
        current_weight -= bridge_weight.popleft()
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge_weight.append(truck_weights.popleft())
        else:
            bridge_weight.append(0)
    
    answer += bridge_length
    return answer
        
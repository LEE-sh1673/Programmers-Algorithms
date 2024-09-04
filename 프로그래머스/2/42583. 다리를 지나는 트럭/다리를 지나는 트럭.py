def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    bridges = deque([0] * bridge_length)
    total_weights = 0
    step = 0
    
    while truck_weights:
        total_weights -= bridges.popleft()
        
        if total_weights + truck_weights[0] > weight:
            bridges.append(0)
        else:
            truck_weight = truck_weights.pop(0)
            total_weights += truck_weight
            bridges.append(truck_weight)
            
        step += 1
        
    return step + bridge_length
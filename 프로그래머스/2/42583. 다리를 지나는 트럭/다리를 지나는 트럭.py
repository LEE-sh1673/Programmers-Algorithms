def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    total_weight = 0
    step = 0
    
    while truck_weights:
        total_weight -= bridge.pop(0)
        
        if total_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            total_weight += truck
        step += 1

    # 이전 단계까지 하여 마지막 트럭이 다리 위에 올라간 상태이다.
    # 따라서 마지막 트럭이 다리를 끝까지 건너는 시간(즉 bridge_length)를 더하면 답이다.
    return step + bridge_length

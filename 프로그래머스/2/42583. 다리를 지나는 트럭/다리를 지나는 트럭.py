"""
1. 트럭 하나가 다리를 건너는데 걸리는 시간 -> 2초


1. 트럭 하나를 큐에서 꺼낸다.
2. 꺼낸 트럭이 다리를 건널 수 있는지 검사한다.
    - 현재 남은 무게 >= 트럭.무게
    - 남은 다리 용량 > 0
3. <2>번에서 조건에 만족하면 트럭을 다리에 집어넣는다.
4. <2>번에서 조건에 만족하지 않으면 다시 큐의 최상단에 집어넣고 1초를 기다린다.
5. 다리에 남아 있는 트럭이 건넜는지 검사한다.
    - 트럭이 다리를 건넜을 경우 다음을 계산한다.
        - 달의 무게 += 트럭의 무게
        - 다라의 허용량 += 1
6. 이후 <1> 과정부터 반복한다.
7. 최종적으로 소요된 시간(초)를 반환한다.

e.g.
trucks(que) = [7,4,5,6]
bridge = 10

[step1]
1. truck = 7
2. weight = 10, capacity = 2
    - 10 >= 7
    - 2 > 0
3. insert bridge -> weight = 3, capacity = 1
4. if timeInSec % bridge_length == 0?
    - ...
4. timeInSec++
...
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque([(truck, 0) for truck in truck_weights])
    bridge = deque([])

    max_weight = weight
    curr_weight = 0

    answer = 0

    while trucks or bridge:
        if trucks:
            truck_weight, dist = trucks[0]

            if not bridge or curr_weight + truck_weight <= max_weight and len(bridge) < bridge_length:
                bridge.append(trucks.popleft())
                curr_weight += truck_weight

        if bridge:
            for _ in range(len(bridge)):
                truck_weight, dist = bridge.popleft()
                bridge.append((truck_weight, dist + 1))

            for _ in range(len(bridge)):
                truck_weight, dist = bridge.popleft()

                if dist < bridge_length:
                    bridge.appendleft((truck_weight, dist))
                    break

                curr_weight -= truck_weight

        answer += 1

    return answer + 1

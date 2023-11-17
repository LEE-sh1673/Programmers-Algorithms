"""
택배상자는 크기가 모두 같음,
1번 상자부터 n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 전달됩니다

만약 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면 
그 상자를 트럭에 실을 순서가 될 때까지 잠시 다른 곳에 보관해야 합니다.

보조 컨테이너 벨트는 앞 뒤로 이동이 가능하지만 입구 외에 다른 면이 막혀 있어서 맨 앞의 상자만 뺄 수 있습니다
보조 컨테이너 벨트를 이용해도 기사님이 원하는 순서대로 상자를 싣지 못 한다면, 더 이상 상자를 싣지 않습니다.

택배 기사님이 알려준 순서: 4 -> 3 -> 1 -> 2 -> 5
영재:
- 1, 2, 3를 보조 컨테이너 벨트에 보관
- 4번째 실음
- 3번째 실음
- 그 다음 1번째 상자를 실어야 하지만 불가능
- 따라서 트럭에는 2개의 상자만 실리게 됨
"""
def solution(order):
    order_boxes = order[::-1]
    sub_boxes = []
    answer = 0
    
    for box in range(1, len(order) + 1):
        sub_boxes.append(box)
        
        while sub_boxes and sub_boxes[-1] == order_boxes[-1]:
            order_boxes.pop()
            sub_boxes.pop()
            answer += 1

    return answer

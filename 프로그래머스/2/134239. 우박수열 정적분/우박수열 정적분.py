"""
우박수의 초항 k와, 정적분을 구하는 구간들의 목록 ranges가 주어졌을 때
정적분의 결과 목록을 return 하도록 solution을 완성해주세요.

단, 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며
이때의 정적분 결과는 -1로 정의합니다.
"""
def area(upper_side, lower_side):
    return (upper_side + lower_side) / 2


def solution(k, ranges):
    target = k
    numbers = [k]
    n = 0
    
    while target > 1:
        if target % 2 == 0:
            target //= 2
        else:
            target = target * 3 + 1
        n += 1
        numbers.append(target)
    
    areas = [area(numbers[0], numbers[1])]
    
    for i in range(1, len(numbers)-1):
        areas.append(area(numbers[i], numbers[i+1]) + areas[i-1])
    areas = [0] + areas
    
    answer = []
    for start, end in ranges:    
        if start > n+end:
            answer.append(-1.0)
        else:
            answer.append(areas[n+end] - areas[start])
    
    return answer


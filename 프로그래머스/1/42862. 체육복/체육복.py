"""
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
이때 이 학생은 체육복을 하나만 도난당했다고 가정, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

e.g. n = 3, lost = [1,3], reserve = [2,3]
3번 도난, 즉 => lost = [1], reserve = [2]
따라서 답은 3
"""
def solution(n, lost, reserve):
    answer = n
    reserve_set = set(reserve)
    lost_set = set(lost)
    
    reserve_lost_set = reserve_set & lost_set
    reserve_set -= reserve_lost_set
    lost_set -= reserve_lost_set
    
    for item in reserve_set:
        if item - 1 in lost_set:
            lost_set.remove(item-1)
        elif item + 1 in lost_set:
            lost_set.remove(item+1)
    
    return answer - len(lost_set)

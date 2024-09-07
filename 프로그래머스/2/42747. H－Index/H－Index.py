def solution(citations):
    answer = 0
    # 논문의 인용 횟수를 내림차 순으로 정렬한다.
    citations = sorted(citations, reverse=True)
    
    # 현재 i번째 논문 c[i]에 대해 c[i] >= i를 만족할 때까지 반복한다. (i >= 1)
    for i, cite in enumerate(citations):
        if cite >= i+1:
            answer += 1
    
    # 위 조건에 만족하는 최대 i를 반환한다.
    return answer
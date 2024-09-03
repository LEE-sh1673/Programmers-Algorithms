"""

1. 각 장르별 분류
    - classic => 0, 2, 3 => [500, 0], [150, 2], [800, 3]
    - pop => 1, 4  => [600, 1], [2500, 4]
2. 재생 횟수를 기준으로 내림차 순 정렬한다.
    - [800, 3], [500, 0], ..
    - ...
3. 각 장르별로 두 개씩 가져온다.
    - [800, 3], [500, 0]
    - [2500, 4], [600, 1]
4. 각 장르별로 선별된 곡을 집어넣는다. 이때 가장 많이 재생된 장르를 먼저 삽입한다.
    - [800, 3], [500, 0] => 1,300
    - [2500, 4], [600, 1] => 3,100
    - [4, 1, 3, 0]
"""
def solution(genres, plays):
    from collections import defaultdict
    
    gs = defaultdict(list)
    for no, gp in enumerate(zip(genres, plays)):
        genre, play = gp
        gs[genre].append([play, no])
    
    for genre in gs.keys():
        gs[genre].sort(key=lambda item : (-item[0], item[1]))
    
    candidates = [gs[genre] for genre in gs.keys()]
    candidates.sort(key=comp)
    
    answer = []
    for candidate in candidates:
        answer += [no for _, no in candidate[:2]]
    return answer

def comp(item):
    total_plays = 0
    min_no = 1e10
    
    for plays, no in item:
        total_plays += plays
        min_no = min(min_no, no)
    return -total_plays, min_no

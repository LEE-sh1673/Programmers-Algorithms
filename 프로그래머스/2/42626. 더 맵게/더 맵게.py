def solution(scoville, K):
    from heapq import heappush, heappop
    answer = 0
    flag = False
    heap = []
    
    for scale in scoville:
        heappush(heap, scale)
        
    if heap[0] >= K:
        return 0
    
    while heap:
        # 가장 낮은 스코빌 지수를 가져온다.
        sc1 = heappop(heap)
        
        if not heap:
            break
    
        # 두 번째로 낮은 스코빌 지수를 가져온다.
        sc2 = heappop(heap)
        
        # 새로운 스코빌 지수를 계산한다.
        new_sc = sc1 + (sc2 * 2)
        
        # 새로운 스코빌 지수를 힙에 넣는다.
        heappush(heap, new_sc)
        
        # 섞은 횟수를 +1 증가시킨다.
        answer += 1
        
        # 모든 스코빌 지수가 7인지 검사한다.
        min_sc = heap[0]
        
        if min_sc >= K:
            flag = True
            break
        
    return answer if flag else -1


# [1, 2, 3]
# 1 + 4 = 5 -> [3, 5]
# 5 + 6 = 11 -> [11]
# 
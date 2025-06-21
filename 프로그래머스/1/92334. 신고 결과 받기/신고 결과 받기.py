def solution(id_list, report, k):
    answer = []
    
    # frodo => 2
    # neo => 2
    # muzi => 1
    # muzi => [frodo: true, neo: true] => 2
    # frodo => [neo: true] => 1
    # apeach => [frodo: true, muzi: false] => 1
    # neo => [?]
    
    # 특정 유저에 대한 정지 여부를 담은 해시 테이블을 만든다.
    # report를 순회하여 각 유저가 신고한 대상이 정지되었을 경우 +1을 매긴다.
    # e.g. { "muzi": 2, "frodo": 1, ...}
    # 해시테이블의 값 리스트만을 반환한다.
    block_users = {user_id: 0 for user_id in id_list}
    results = {user_id: set() for user_id in id_list}
    
    for r_info in set(report):
        user, block_user = r_info.split(' ')
        block_users[block_user] += 1
        results[user].add(block_user)
        
    for ke, v in results.items():
        answer.append(sum([1 if block_users[u] >= k else 0 for u in v]))
        
    
    return answer
'''

요금표:
- 기본시간
- 기본요금
- 단위시간
- 단위요금

자동차별 주차 요금 (누적_주차_시간_분, 차량표) -> 주차 요금
    return 기본 요금 + [ (누주시분 - 기본 시간) / 단위 시간] * 기본 요금
    
누주시분
- 입차 후 출차 시간 X -> (23:59 - 입차)
- 누주시분 <= 기본 시간 -> 기본 요금
- 누주시분 > 기본 시간 -> 

차량번호 오름차순으로 주차요금반환

- records에서 (시각, 차량번호, 내역)을 추출한다.
- 각 차량번호에 해당하는 차량정보를 조회한다.
- 차량정보가 있다면 해당 정보를 (시각, 내역)으로 갱신 요청한다.
    - 내역 == 'IN':
        - 시각 정보 * -1
    - 내역 == 'OUT':
        - 시각 정보 * 1
- 각 차량들에 대한 주차 요금을 계산한다.
- 차량 번호가 작은 순으로 주차 요금 배열을 반환한다.
'''
from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    
    def time_to_minutes(time):
        h, m = time.split(':')
        return int(h) * 60 + int(m)
    
    for record in records:
        time, no, stat = record.split()
        minutes = time_to_minutes(time)
        minutes = -minutes if stat == 'IN' else minutes
        cars[no].append([stat, minutes])
    
    t, c, u, uc = fees
    
    for no in cars.keys():
        total = sum([minutes for _, minutes in cars[no]])
        total = 1439 +  total if cars[no][-1][0] == 'IN' else total
        
        if total > t:
            total = c + (ceil((total - t) / u)) * uc
        else:
            total = c
        
        answer.append([no, total])
    
    answer.sort(key=lambda x: x[0])
    return [total for _, total in answer]
"""
LV2. [1차] 캐시
[https://school.programmers.co.kr/learn/courses/30/lessons/17680]

풀이:
1. 도시 이름을 대문자 or 소문자로 변환한다.
2. 도시와 캐시에 대해 다음을 진행한다.
	
  A. cache hit:
    - 실행 시간을 +1한다.
    - cache hit 된 도시가 캐시의 뒤(rear)에 오도록 순서를 조정한다.
    
  B. cache miss:
    - 실행 시간을 +5한다.
    - 캐시의 뒤(rear)에 도시를 추가한다.

3. 캐시 크기에 따라 다음을 진행한다.
  
  3.1 len(캐시) >= cacheSize:
    - 캐시의 앞(front)에 있는 도시를 삭제한다.
  
4. 계산된 실행 시간을 반환한다.
"""


class CacheStat:
    CACHE_HIT = 1
    CACHE_MISS = 5

    
class ExecutionTimeMeter(CacheStat):
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = []
        self.exec_time = 0
    
    def meter(self, items):
        for item in items: 
            self.add(item.upper())
        return self.exec_time
    
    def add(self, item):
        hit = self.is_hit(item)
        self.exec_time += (self.CACHE_HIT if hit else self.CACHE_MISS)
        
        if hit:
            self.move_to_rear(item)
            return
        
        self.cache.append(item)
        self.update_cache()
        
    def is_hit(self, item):
        return item in self.cache
    
    def move_to_rear(self, item):
        if (idx := self.cache.index(item)) >= 0:
            self.cache.append(self.cache.pop(idx))
		
    def update_cache(self):
        if len(self.cache) > self.cache_size:
            self.cache.pop(0)        


def solution(cacheSize, cities):
    exec_time_meter = ExecutionTimeMeter(cacheSize)
    return exec_time_meter.meter(cities)
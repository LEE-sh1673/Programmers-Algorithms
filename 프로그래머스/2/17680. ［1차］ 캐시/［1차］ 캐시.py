"""
LV2. [1차] 캐시
[https://school.programmers.co.kr/learn/courses/30/lessons/17680]

풀이:
1. 도시 이름을 대문자 or 소문자로 변환한다.
2. 각 도시에 대해 다음을 진행한다.

  A. cache hit:
    - cache hit 된 도시가 캐시의 뒤(rear)에 오도록 순서를 조정한다.
    - 실행 시간을 +1한다.
    
  B. cache miss:
    - 캐시의 뒤(rear)에 도시를 추가한다.
    - 캐시 크기에 따라 다음을 진행한다.

      B.A len(캐시) > cacheSize:
        - 캐시의 앞(front)에 있는 도시를 삭제한다.

    - 실행 시간을 +5한다.
  
3. 계산된 실행 시간을 반환한다.
"""


class CacheStat:
    CACHE_HIT = 1
    CACHE_MISS = 5


class LRUCache(CacheStat):
    def __init__(self, capacity):
        self.cache = []
        self.capacity = capacity

    def put(self, item):
        hit = self.is_hit(item)
        self.adjust(item, hit)
        return self.CACHE_HIT if hit else self.CACHE_MISS

    def is_hit(self, item):
        return item in self.cache

    def adjust(self, item, hit):
        if hit:
            self.move_to_end(item)
            return        
        self.add(item)

    def add(self, item):
        self.cache.append(item)
        
        if len(self.cache) > self.capacity:
            self.cache.pop(0)
    
    def move_to_end(self, item):
        if (idx := self.cache.index(item)) >= 0:
            self.cache.append(self.cache.pop(idx))


class ExecutionTimeMeter:
    def __init__(self, cache_size):
        self.cache = LRUCache(cache_size)

    def meter(self, items):
        return sum([self.cache.put(item.upper()) for item in items])


def solution(cacheSize, cities):
    exec_time_meter = ExecutionTimeMeter(cacheSize)
    return exec_time_meter.meter(cities)

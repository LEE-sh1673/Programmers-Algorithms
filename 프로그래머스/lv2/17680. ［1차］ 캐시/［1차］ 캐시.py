class CacheItem:
    def __init__(self, val):
        self.val = val
        self.references = 0
    
    def get_nums_references(self):
        return self.references
        
    def increase_references(self):
        self.references += 1
        
    def reset_references(self):
        self.references = 0

    def __lt__(self, other):
        return self.references < other.references
        
    def __eq__(self, other):
        return (self.val) == (other.val)
    
    def __repr__(self):
        return f'item({self.val}, {self.references})'

class CacheMeter:
    def __init__(self, cache_size):
        self.cache = []
        self.exec_time = 0
        self.cache_size = cache_size
    
    def is_hit(self, item):
        return item in self.cache
    
    def update_cache(self):
        if self.is_full():
            self.cache.pop(0)
        
    def add(self, item):
        if self.is_hit(item):
            self.exec_time += 1
            self.move_to_front(item)
        else:
            self.exec_time += 5
            self.cache.append(item)
        self.update_cache()
    
    def move_to_front(self, item):
        if (idx := self.cache.index(item)) >= 0:
            self.cache.append(self.cache.pop(idx))
        
    def is_full(self):
        return len(self.cache) > self.cache_size
        
    def meter(self, items):
        for item in items:
            self.add(CacheItem(item.upper()))
        return self.exec_time

    
def solution(cacheSize, cities):
    cache_meter = CacheMeter(cacheSize)
    return cache_meter.meter(cities)
                             
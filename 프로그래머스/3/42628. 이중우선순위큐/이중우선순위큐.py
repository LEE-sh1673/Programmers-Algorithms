class DblEndedPQ:
    def __init__(self):
        self.items = set()
    
    def size(self):
        return len(self.items)
    
    def put(self, item):
        self.items.add(item)
    
    def get_min(self):
        return min(self.items) if self.items else 0

    def get_max(self):
        return max(self.items) if self.items else 0
    
    def remove_min(self):
        if not self.items:
            return
        self.items.remove(self.get_min())
        
    def remove_max(self):
        if not self.items:
            return
        self.items.remove(self.get_max())

    
def solution(operations):
    heap = DblEndedPQ()
    
    for cv in operations:
        if cv == 'D 1':
            heap.remove_max()
        elif cv == 'D -1':
            heap.remove_min()       
        else:
            heap.put(int(cv[2:]))
            
    return [heap.get_max(), heap.get_min()]




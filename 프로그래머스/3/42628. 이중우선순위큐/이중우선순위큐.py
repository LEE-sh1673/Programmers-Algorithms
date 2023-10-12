class PriorityQueue:
    def __init__(self):
        self.que = set()
    
    def insert(self, item):        
        self.que.add(item)
        
    def remove_max(self):
        if self.que:
            self.que.discard(max(self.que))
    
    def remove_min(self):
        if self.que:
            self.que.discard(min(self.que))
            
    def max(self):
        return max(self.que) if self.que else 0

    def min(self):
        return min(self.que) if self.que else 0
        
    def __repr__(self):
        return f'queue ({self.que})'


def solution(operations):
    answer = []
    q = PriorityQueue()
    
    for operation in operations:
        cmd, val = operation.split()
        
        if cmd == 'I':
            q.insert(int(val))
        elif cmd == 'D':
            q.remove_max() if val == '1' else q.remove_min()
        
    return [q.max(), q.min()]
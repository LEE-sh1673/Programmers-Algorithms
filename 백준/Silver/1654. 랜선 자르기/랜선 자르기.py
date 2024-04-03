from sys import stdin

input = stdin.readline
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]


def find(low, high):
    while low < high:   
        mid = low + (high - low) // 2
        line_count = sum([line // mid for line in lines])
        
        if line_count >= n:  
            low = mid + 1
        else:
            high = mid
    return low - 1


print(find(0, max(lines)+1))

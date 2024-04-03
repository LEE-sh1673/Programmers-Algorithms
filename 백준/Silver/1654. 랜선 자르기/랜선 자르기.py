from sys import stdin

input = stdin.readline
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
standard = max(lines)
answer = 0


def binary(low, high):
    global n, answer

    while low <= high:   
        mid = low + (high - low) // 2
        line_count = sum([line // mid for line in lines])
        
        if line_count >= n:
            answer = mid   
            low = mid + 1
        else:
            high = mid-1
        
binary(0, standard * 2)
print(answer)

# def solution(n):
#     if n < 2:
#         return n

#     k = (n + 1) // 2 + 1
#     answer = 0

#     for i in range(1, k):
#         total = 0
#         j = i
        
#         while total < n:
#             total += j
#             j += 1

#         answer = answer + 1 if total == n else answer

#     return answer + 1
# logN * N

def solution(n):
    cnt = 0
    k = int((n // 2) + 1)

    for i in range(1, k):
        for j in range(i + 1, n):
            i += j
            
            if i > n:
                break
            elif i == n:
                cnt += 1
                break
    
    return cnt + 1
    
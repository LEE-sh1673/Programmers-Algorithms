def solution(triangle):
    H = len(triangle)
    d = [[0] * (i+1) for i in range(H-1)] + [triangle[-1]]

    for i in range(H-2, -1, -1):
        for j in range(len(triangle[i])):
            d[i][j] = triangle[i][j] + max(d[i+1][j], d[i+1][j+1])
    
    return d[0][0]
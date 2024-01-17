def rotate(matrix, query):
    query = [pos - 1 for pos in query]
    tmp = matrix[query[0]][query[1]]
    min_val = tmp
    
    # 아래 -> 왼
    for i in range(query[0], query[2]):
        matrix[i][query[1]] = matrix[i+1][query[1]]
        min_val = min(min_val, matrix[i+1][query[1]])
    
    # 오 -> 왼
    for i in range(query[1], query[3]):
        matrix[query[2]][i] = matrix[query[2]][i+1]
        min_val = min(min_val, matrix[query[2]][i+1])
        
    # 위 -> 아래
    for i in range(query[2], query[0], -1):
        matrix[i][query[3]] = matrix[i-1][query[3]]
        min_val = min(min_val, matrix[i-1][query[3]])
    
    # 왼 -> 오
    for i in range(query[3], query[1], -1):
        matrix[query[0]][i] = matrix[query[0]][i-1]
        min_val = min(min_val, matrix[query[0]][i-1])
    
    matrix[query[0]][query[1]+1] = tmp;
    return min_val


def solution(rows, columns, queries):
    matrix = [list() for i in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            matrix[i].append(i * columns + j + 1)
    
    answer = []
    for query in queries:
        answer.append(rotate(matrix, query))    
    return answer

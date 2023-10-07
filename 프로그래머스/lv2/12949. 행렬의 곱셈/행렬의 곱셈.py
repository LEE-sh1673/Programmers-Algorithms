def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        k_arr = []
        for j in range(len(arr2[0])):
            total = sum([arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))])
            k_arr.append(total)
        answer.append(k_arr)
        
    return answer
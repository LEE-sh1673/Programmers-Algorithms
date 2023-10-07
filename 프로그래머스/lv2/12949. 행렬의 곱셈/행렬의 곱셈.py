def solution(arr1, arr2):
    answer = []

    for arr1_col in arr1:
        k_arr = []
        for arr2_row in zip(*arr2):
            k_arr.append(sum([el1 * el2 for el1, el2 in zip(arr1_col, arr2_row)]))
        answer.append(k_arr)

    return answer

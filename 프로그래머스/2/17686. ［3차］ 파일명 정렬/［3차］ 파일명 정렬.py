def solution(files):
    answer = []

    # 비교 시 수행
    # 1. 대소문자를 통일한다.
    # 2. 숫자 앞에 0을 무시한다.
    # 3. 정렬 기준은 1. 영문자 -> 2. 숫자이다.
    # 4. 그 외의 것들은 무시한다.

    for idx, file in enumerate(files):
        head, number = split_head_number(file)
        answer.append([head, number, file])

    answer = sorted(answer, key=lambda item: (item[0].lower(), item[1]))
    return [file[-1] for file in answer]



def split_head_number(file):
    n = len(file)
    start_idx = next(idx for idx, ch in enumerate(file) if ch.isdigit())
    
    number_idx = start_idx
    
    while number_idx < n:
        try:
            int(file[number_idx])
            number_idx += 1
        except:
            break
            
    return file[:start_idx], int(file[start_idx:number_idx])


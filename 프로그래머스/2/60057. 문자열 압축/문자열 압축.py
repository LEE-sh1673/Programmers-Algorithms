# def solution(s):
#     s_length = len(s)
#     min_length = s_length
    
#     # 문자열의 길이가 1 또는 0인 경우 그대로 반환합니다.
#     if s_length == 1 or s_length == 0:
#         return s_length
    
#     # 문자열 길이를 1 ~ N/2 까지 압축시키고 그 길이를 저장합니다.
#     for tok_len in range(1, s_length//2 + 1):
#         words = [s[i:i+tok_len] for i in range(0, s_length, tok_len)]
#         compressed = []
#         curr_count = 1
        
#         for A, B in zip(words, words[1:] + ['']):
#             if A == B:
#                 curr_count += 1
#             else:
#                 compressed.append([curr_count, A])
#                 curr_count = 1
                
#         compressed_length = sum((len(str(count)) if count != 1 else 0) + len(word)  for count, word in compressed)

#         if min_length >= compressed_length:
#             min_length = compressed_length
    
#     # 가장 작은 길이를 반환합니다.
#     return min_length


def solution(s):
    str_length = len(s)

    if str_length <= 1:
        return str_length

    min_length = str_length

    for i in range(1, str_length//2 + 1, 1):
        token_str = [s[j:j+i] for j in range(0, str_length, i)]
        curr_cnt = 1
        res = []

        for curr_word, next_word in zip(token_str, token_str[1:]+ ['']):
            if curr_word == next_word:
                curr_cnt += 1
            else:
                res.append([curr_word, curr_cnt])
                curr_cnt = 1

        curr_length = sum([len(word) + (len(str(cnt)) if cnt != 1 else 0) for word, cnt in res])

        if curr_length < min_length:
            min_length = curr_length

    return min_length
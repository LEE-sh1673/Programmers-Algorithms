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
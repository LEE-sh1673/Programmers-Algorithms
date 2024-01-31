"""
"aabbaccc" -> "aa", "bb", "a", "ccc" -> "2a2ba3c"

문자를 1개 단위로 자르는 경우:
aa => 2
ab => 2a
bb => 2 
ba => 2b
ac => 1a
cc => 2
cc => 3
c => 3c

"ababcdcdababcdcd" -> "abab", "cdcd", "abab" -> "cdcd" -> "2ab2cd2ab2cd"
"ababcdcdababcdcd" -> "ababcdcd / ababcdcd" -> "2ababcdcd"

- 이때 최대로 자를 수 있는 단위는 len(s)/2
""" 
def solution(s):
    if (str_length := len(s)) <= 1:
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

        curr_length = sum([len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res])
        min_length = min(min_length, curr_length)

    return min_length

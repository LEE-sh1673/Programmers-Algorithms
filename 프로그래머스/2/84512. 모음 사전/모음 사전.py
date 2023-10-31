def solution(word):
    answer = 0
    cnt = 0
    
    def dfs(w, target):
        nonlocal cnt
        nonlocal answer

        if w == target:
            answer = cnt

        if len(w) > 5:
            return

        cnt += 1
        for ch in 'AEIOU':
            dfs(w + ch, target)

    dfs("", word)
    return answer

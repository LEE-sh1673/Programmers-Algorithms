"""
""
|\
A E ...
|
AA ...
|
AAA ...
|   \
AAAA AAAE -&(AAAEA ... AAAEU)
|
&(AAAAA, ... AAAAE)

- 자릿수 5까지 반복, 자릿수 > 5라면 자릿수를 하나 줄이고 다음 알파벳으로 대체 
- 알파벳 문자열이 반복되는 구조가 DFS 탐색의 흐름과 동일
"""
def solution(word):
    keywords = 'AEIOU'
    answer = 0
    cnt = 0
    
    def dfs(w):
        nonlocal answer
        nonlocal cnt
            
        if w == word:
            answer = cnt
            return 

        if len(w) >= 5:
            return
        
        for keyword in keywords:
            cnt += 1
            dfs(w + keyword)
    
    dfs("")
    return answer

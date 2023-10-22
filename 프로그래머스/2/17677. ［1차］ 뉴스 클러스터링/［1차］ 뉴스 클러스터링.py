"""    
// J(A, B)
// = 교집합 크기 / 합집합 크기
// J(x, x)
// = 1 (두 집합이 모두 공집합일 경우)
//
// J(A, B)
// - 교집합: min(count_A, count_B)
// - 합집합: max(count_A, count_B)
//
// e.g.s
// A = {1, 1, 2, 2, 3}
// B = {1, 2, 2, 4, 5}
// A n B = {1, 2, 2}
// A u B = {1, 1, 2, 2, 3, 4, 5}
// 3 / 7 ~ 0.42

// 1. 자카드 유사도 집합 만들기
// - 각 집합을 소문자/대문자로 변환
// - 크기를 2만큼 각각 슬라이싱 한다.
// - 슬라이싱된 각 요소를 검사한다.
//  - 영문자로된 글짜 쌍이 아니면 버린다.

// 2. 자카드 유사도 교집합 만들기
// - A 집합의 카운트를 구한다.
// - B 집합의 카운트를 구한다.
// - A[i] == B[i] 인 경우를 구한다.
//  - min(A[i].count, B[i].count)

// 2. 자카드 유사도 합집합 만들기
// - A 집합의 카운트를 구한다.
// - B 집합의 카운트를 구한다.
// - 모든 집합을 합친다.
// - A[i] == B[i] 인 경우를 아래를 수행
//  - max(A[i].count, B[i].count)

// J(A, B)
// 1. 유사도 집합 만들기
// 2. 교집합 만들기
// 3. 합집합 만들기
// 4. 교집합 // 합집합
"""
from collections import Counter
import re


def solution(str1, str2):    
    # 1. 자카드 유사도 집합 만들기
    s1_set = make_set(str1)
    s2_set = make_set(str2)
    
    if s1_set == [] and s2_set == []:
        return 65536
        
    s1_cnt = Counter(s1_set)
    s2_cnt = Counter(s2_set)

    # 2. 교집합 만들기    
    diff_set = []
    for a in s1_cnt:
        if a in s2_cnt:
            diff_set += [a] * min(s1_cnt[a], s2_cnt[a])
    
    # 3. 합집합 만들기     
    union_set = [el for el in s1_set + s2_set if el not in diff_set]
    
    for a in s1_cnt:
        if a in s2_cnt:
            union_set += [a] * max(s1_cnt[a], s2_cnt[a])
    
    return int(len(diff_set) / len(union_set) * 65536)


def make_set(word):
    return [w.lower() for i in range(len(word)-1) if (w := word[i:i+2]).isalpha()]


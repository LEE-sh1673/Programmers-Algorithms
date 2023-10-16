from collections import defaultdict

def count_diff_letters(word1, word2):
    return sum([w1 != w2 for w1, w2 in zip(word1, word2)])


def dfs(g, word, target, trace = []):
    if word == target:
        return len(trace)

    if word in trace:
        return 0

    results = []

    for w in g[word]:
        r = dfs(g, w, target, trace + [word])

        if r != 0:
            results.append(r)

    return min(results) if results else 0


def solution(begin, target, words):
    g = defaultdict(list)

    for i in words + [begin]:
        g[i] = [w for w in words if i != w and count_diff_letters(i, w) == 1]

    return dfs(g, begin, target)

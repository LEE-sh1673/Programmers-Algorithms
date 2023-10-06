def solution(citations):
    citations.sort(reverse=True)
    return next((i for i, citation in enumerate(citations) if i >= citation), len(citations))

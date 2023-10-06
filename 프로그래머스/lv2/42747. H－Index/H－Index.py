def solution(citations):
    if all(citation == 0 for citation in citations):
        return 0
    
    citations.sort(reverse=True)
    return next((i for i, citation in enumerate(citations) if i >= citation), len(citations))

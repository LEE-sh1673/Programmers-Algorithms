def solution(citations):
    citations.sort(reverse=True)
    
    h = 0
    
    for citation in citations:
        if h >= citation:
            break
        h += 1
    
    return h
    
    # return next((h for h, citation in enumerate(citations) if h >= citation), len(citations))

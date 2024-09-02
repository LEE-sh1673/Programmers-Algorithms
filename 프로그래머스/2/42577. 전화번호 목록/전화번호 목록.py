def solution(phone_book):
    phone_book.sort()
    curr = phone_book[0]
    
    # 12 13
    
    for num in phone_book[1:]:
        if curr != num[:len(curr)]:
            curr = num
        else:
            return False
        
    return True

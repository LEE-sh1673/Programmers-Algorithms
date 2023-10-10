# def solution(want, number, discount) -> bool:
#     return sum(is_all_discounted(want, number, discount[day:day + 10]) for day in range(len(discount)))


# def is_all_discounted(want, number, discount) -> bool:
#     return all(discount.count(product) >= quantity for product, quantity in zip(want, number))

from collections import Counter

def solution(want, number, discount):
    answer = 0
    wishList = {}
    
    for i in range(len(want)) :
        wishList[want[i]] = number[i]
    
    for i in range(len(discount)-9) :
        c = Counter(discount[i:i+10])
        
        if ( c == wishList) :
            answer += 1
            
    return answer
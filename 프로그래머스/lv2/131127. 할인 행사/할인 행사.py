def solution(want, number, discount):
    answer = 0
    for day in range(len(discount)):
        if all_discounted(day, want, number, discount):
            answer += 1
    return answer


def all_discounted(day, want, number, discount):
    return all(discounted(product, quantity, discount[day:day+10]) for product, quantity in zip(want, number))


def discounted(product, quantity, discount) -> bool:
    return discount.count(product) >= quantity
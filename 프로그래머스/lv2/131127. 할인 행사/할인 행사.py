def solution(want, number, discount) -> bool:
    return sum(is_products_discounted(want, number, discount[day:day + 10]) for day in range(len(discount)))


def is_products_discounted(want, number, discount) -> bool:
    return all(is_product_discounted(product, quantity, discount) for product, quantity in zip(want, number))


def is_product_discounted(product, quantity, discount) -> bool:
    return discount.count(product) >= quantity
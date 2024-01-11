def solution(storey):
    answer = 0

    while storey:
        q, r = divmod(storey, 10)

        if r > 5:
            answer += (10 - r)
            storey += 10
        elif r < 5:
            answer += r
        else:
            if q % 10 > 4:
                storey += 10
            answer += r

        storey //= 10

    return answer
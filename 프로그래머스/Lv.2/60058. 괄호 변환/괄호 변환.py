def convert(w: str) -> str:
    if w == '' or is_correct(w):
        return w

    u, v = split_uv(w)

    if is_correct(u):
        return u + convert(v)

    return '(' \
        + convert(v) \
        + ')' \
        + reverse_brackets(u[1:-1])


def is_correct(w: str) -> bool:
    cnt: int = 0
    return all(
        (cnt := cnt + 1 if ch == '(' else cnt - 1) >= 0
        for ch in w
    )

    
def split_uv(w: str) -> tuple:
    cnt: int = 0

    for i, ch in enumerate(w):
        cnt += 1 if ch == '(' else -1

        if cnt == 0:
            return w[:i+1], w[i+1:]

    return '', ''


def reverse_brackets(w: str) -> str:
    table = str.maketrans("()", ")(")
    return w.translate(table)

    
def solution(w):
    return convert(w)

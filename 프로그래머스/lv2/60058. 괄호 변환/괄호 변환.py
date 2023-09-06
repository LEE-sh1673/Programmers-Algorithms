class BracketConverter:
    def convert(self, w: str) -> str:
        if w == '' or self.is_correct(w):
            return w

        u, v = self.split_uv(w)

        if self.is_correct(u):
            return u + self.convert(v)

        return '(' \
            + self.convert(v) \
            + ')' \
            + self.reverse_brackets(u[1:-1])

    @classmethod
    def is_correct(cls, w: str) -> bool:
        cnt: int = 0
        return all(
            (cnt := cnt + 1 if ch == '(' else cnt - 1) >= 0
            for ch in w
        )

    @classmethod
    def split_uv(cls, w: str) -> tuple:
        cnt: int = 0

        for i, ch in enumerate(w):
            cnt += 1 if ch == '(' else -1

            if cnt == 0:
                return w[:i+1], w[i+1:]

        return '', ''

    @classmethod
    def reverse_brackets(cls, w: str) -> str:
        table = str.maketrans("()", ")(")
        return w.translate(table)

    
def solution(w: str) -> str:
    converter: BracketConverter = BracketConverter()
    return converter.convert(w)
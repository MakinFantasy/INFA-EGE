from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 3)


@lru_cache(None)
def f(h):
    if sum(h) >= 69:
        return 'end'
    elif any(f(x) == 'end' for x in moves(h)):
        return 'p1'
    elif any(f(x) == 'p1' for x in moves(h)):
        return 'v1'


for i in range(1, 100):
    h = 10, i
    print(i, f(h))

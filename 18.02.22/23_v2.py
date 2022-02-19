def k(x, y):
    if x == y:
        return 1
    if x > y or x == 8 or x == 11:
        return 0
    if x < y:
        return k(x + 1, y) + k(x + 2, y) + k(x * 2, y)


print(k(3, 10) * k(10, 12))

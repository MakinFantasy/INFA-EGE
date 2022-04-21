def sraka(a, b, n):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif n == 2:
        return sraka(a+1, b, n)
    else:
        return sraka(a+1, b, n) + sraka(a * 2, b, n+1)
print(sraka(1, 11, 0))

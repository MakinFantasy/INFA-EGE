def f(n):
    if n > 0:
        f(n//4)
        print(n)
        f(n-1)


f(5)

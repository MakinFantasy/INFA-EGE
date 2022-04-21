def f(a, b):
    if a == 0:
        return b
    elif a > 0:
        return f(a//10, 10*b + (a % 10))


for a in range(1, 10**10):
    if f(a, 0) == 1248163264:
        print(a)
        break

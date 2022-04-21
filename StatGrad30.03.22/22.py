maxb = 0
for i in range(1, 1000000):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d
        x //= 10
    if a == 6300:
        maxb = max(maxb, b)
print(maxb)
# Ответ: 19

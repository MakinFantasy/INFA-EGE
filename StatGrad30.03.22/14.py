n = 7 * 729**6 + 6 * 81**9 + 3**14 - 90
counter = 0
while n > 0:
    if (n % 9) % 2 == 0:
        counter += 1
    n = n // 9
print(counter)

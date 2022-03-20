def f(bebra):
    if bebra == 0:
        return 0
    elif bebra % 2 != 0:
        return f(bebra - 1) + 1
    else:
        return f(bebra // 2)

for i in range(1, 100):
    print(i, bin(i)[2:], f(i))


print(bin(10**9)) ### миллиадр в двоичной
print(2**30) ### проверка 
print(2**29)
print(15 * 29)
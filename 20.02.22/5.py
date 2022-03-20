
for i in range(1, 5000):
    new_num = str()
    num = i
    while num > 0:
        new_num = str(num % 2) + new_num
        num = num // 2
    if new_num == '1111111111':
        print(i)
        break

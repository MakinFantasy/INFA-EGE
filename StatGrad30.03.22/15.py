mindl = 10000
for a1 in range(50, 350):
    for a2 in range(a1 + 1, 530):
        flag = False
        for x in range(60, 520):
            if (((180<=x<=520) == (60<=x<=450)) or (((60<=x<=450) and (not(180<=x<=520))) <= (a1<=x<=a2))) == False:
                flag = True
                break
        if flag == False:
            dl = a2 - a1
            mindl = min(dl, mindl)
print(mindl/10)
# увеличили числа в 10 раз, чтобы были дроби
# 11.9 -> 12
# Ответ: 12

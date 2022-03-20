p1 = 3 ### 6 symbols, 6 < 2 ** 3, so we have 3 bits.
p2 = 55 ### 1) 20 letters, 20 < 2 ** 5, so we have 5 bits. 2) 11 symbols, sp we mutiplicate 5 on 11 and get 55 bits.
p3 = 11 ### 1 - 1999. At all 1999 numbers, 1999 < 2**11, so we have 11 bits.
p_sum = p1 + p2 + p3
print(p_sum)
v_p = round(p_sum / 8) ### Without round() we get 8.625, and we need to rund to max bits.
print(v_p)
v = 1188
for i in range(1, 10000):
    if (v_p + i) * 36 == v:
        print(i)

from itertools import product

counter = 0
for x in product('НАСТЯ', repeat=7):
    s = ''.join(x)
    if s.count('Н') == 2 and s.count('А') >= 1:
        counter += 1
print(counter)

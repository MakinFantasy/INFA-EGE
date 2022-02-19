from itertools import product

counter = 0

for i in product('ОНИКС', repeat=4):
    if i.count('С') == 3 and i.count('О') == 1:
        counter += 1

for i in product('ОНИКС', repeat=5):
    if i.count('С') == 3 and i.count('О') == 1:
        counter += 1

for i in product('ОНИКС', repeat=6):
    if i.count('С') == 3 and i.count('О') == 1:
        counter += 1

print(counter)

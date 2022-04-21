from itertools import product

counter = 0

for i in product('ОНИКС', repeat=4):
    if i.counter('С') == 3 and i.counter('О') == 1:
        counter += 1

for i in product('ОНИКС', repeat=5):
    if i.counter('С') == 3 and i.counter('О') == 1:
        counter += 1

for i in product('ОНИКС', repeat=6):
    if i.counter('С') == 3 and i.counter('О') == 1:
        counter += 1

print(counter)

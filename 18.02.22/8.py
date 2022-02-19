### Номер слова. Дан список, слова пронумерованы

letters = 'ЕЛМРУ'
l = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                l.append(a + b + c + d)
print(l.index('ЛЕЕЕ') + 1)

alf = 'НАСТЯ'
counter = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            s = x1+x2+x3+x4+x5+x6+x7
                            if s.count('Н') == 2 and s.count('А') >= 1:
                                counter += 1
print(counter)

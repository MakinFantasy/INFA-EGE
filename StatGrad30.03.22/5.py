for i in range(1, 10000):
    sch = str(i)
    maxim = 0
    minim = 100
    for j in range(len(sch) - 1):
        tch = int(sch[j] + sch[j+1])
        maxim = max(tch, maxim)
        minim = min(tch, minim)
    if maxim + minim == 137:
        print(i, maxim, minim)
        break

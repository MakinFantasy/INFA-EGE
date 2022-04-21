# i = 7_000_000 + 1
def delit(n):
    d = 2
    mas = []
    while d * d < n :
        if n % d == 0:
            mas.append(d)
            mas.append(n // d)
        d += 1
    if d * d == n:
        mas.append(d)
    return mas


def prov(a, n):
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            for z in range(y + 1, len(a)):
                if a[x] * a[y] * a[z] == n:
                    return False
    return True


counter = 0
for k in range(1, 10**10):
    num = 7_000_000 + k
    vse_d = delit(num)
    if prov(vse_d, num):
        print(num, k)
        counter += 1
        if counter == 5:
            break

f = open('27-A.txt')
n = int(f.readline())
res = 0
mas = []
for i in range(n):
    x = int(f.readline())
    mas.append(x)
for i in range(len(mas) - 100):
    for j in range(i + 100, len(mas)):
        st = 0
        for z in range(i, j+1):
            st += mas[z]
        if st % 999 == 0:
            res += 1
print(res)

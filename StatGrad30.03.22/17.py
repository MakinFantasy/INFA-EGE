with open('17.txt') as f:
    a = list(map(int, f.readlines()))
minn = 10001
for i in range(len(a)):
    if a[i] % 2 != 0:
        minn = min(minn, a[i])
counter = 0
maxabs = -1
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 and a[i+1] % 3 != 0) or (a[i+1] % 3 == 0 and a[i] % 3 != 0):
        if abs(a[i] - a[i+1]) < minn:
            counter += 1
            maxabs = max(abs(a[i] - a[i+1]), maxabs)
print(counter, maxabs)

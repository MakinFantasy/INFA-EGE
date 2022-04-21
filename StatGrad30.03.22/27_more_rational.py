k = 999
dl = 100
f = open('27-A.txt')
n = int(f.readline())
res = 0
pref = [0] * k
tyrma = []
st = 0
s_levee_tyrma = 0
for i in range(dl + 1):
    x = int(f.readline())
    tyrma.append(x)
    st += x
if st % k == 0:
    res += 1
for i in range(n - dl - 1):
    s_levee_tyrma += tyrma[0]
    pref[s_levee_tyrma % k] += 1
    x = int(f.readline())
    st += x
    tost = st % k
    if st % k == 0:
        res += 1
    res += pref[tost]
    del tyrma[0]
    tyrma.append(x)
print(res)

# 27-A.txt is example file

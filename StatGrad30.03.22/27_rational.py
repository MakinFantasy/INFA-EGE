k = 3 # is example sum
ots = 100
f = open('27-A.txt')
n = int(f.readline())
res = 0
pref = [0] * k
st = 0
for i in range(n):
    x = int(f.readline())
    st += x  # find current sum
    tost = st % k  # mod of current sum
    if st % k == 0:  # if current sum is good for usm then we raise counter
        res += 1
    res += pref[tost]  # sum counter with pref sums with the same mod
    pref[tost] += 1  # raise pref sum
print(res)

# 27-A.txt is example file

f = open('24.txt')
s = f.readline()
print(s)
s = s.split('A')
print(s)
k = 0
for i in range(1, len(s) - 1):
    if s[i].count('B') >= 2 and len(s[i]) >= 10:
        k += 1
print(k)
# 24.txt - Example

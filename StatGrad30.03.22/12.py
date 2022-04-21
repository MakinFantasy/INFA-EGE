s = '0' + 8 * '2' + 9 * '121' + 5 * '1' + '0'
while '00' not in s:
    s = s.replace('021', '102', 1)
    s = s.replace('022', '301', 1)
    s = s.replace('02', '20', 1)
    s = s.replace('01', '10', 1)
print(s)
print(s.count('1'), s.count('2'), s.count('3'))

a, f, i = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'], 0, 0
p, r = pydle, range

for y in r(2):
    for x in r(5):
        p(x, y, a[i], 'red')
        i += 1

i -= 1

for y in r(3, 5):
    for x in r(5):
        p(x, y, a[i], 'blue')
        i -= 1

i = 10

for x in r(5):
    p(x, 2, a[i], 'white')
    if i == 12: f = 1
    i = i + 1 if f == 0 else i - 1
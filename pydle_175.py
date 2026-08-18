p, r, b, w = pydle, range, 'blue', 'white'

for x in r(5):
    for y in r(5): p(x, y, '', b)

for x in r(0, 5, 4):
    for y in r(0, 5, 4): p(x, y, '', w)

for x in r(5):
    if x != 2: p(x, 1, '', w)

for x in r(1, 4, 2): p(x, 2, '', w)

p(2, 0, '●', b)
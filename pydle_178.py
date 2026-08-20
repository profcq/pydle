r, p, v, i = range, pydle, '', 0;

for x in r(5):
    for y in r(3):
        p(x, y, v, 'blue')

for x in r(1, 4, 2):
    for y in r(3, 5):
        p(x, y, v, 'yellow')

for y in r(3, 0, -1):
    for x in r(i, 5, 2):
        p(x, y - 1, v, 'white')
        if y - 1 == 0: break

    i += 1

p(4, 3, 'o', v)
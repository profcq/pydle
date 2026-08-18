r, p, b, n, m = range, pydle, '', 4, 'brown'

for x in r(5):
    for y in r(5):
        p(x, y, b, 'red')

for x in r(3):
    for y in r(n):
        p(x, y, b, 'purple')

    n = 3 if x == 0 else 1

for x in r(4, 5):
    for y in r(5):
        p(x, y, b, m)

p(3, 0, b, m)

for y in r(1, 5, 3): p(0, y, b, 'white')
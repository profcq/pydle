r, p = range, pydle
w, i, s = 'white', 1, 2

for x in r(5):
    for y in r(5):
        p(x, y, '', w)

for y in r(5):
    for x in r(i, 4, s):
        p(x, y, '❤️', w)

    if i == 1: i, s = 2, 3
    else: i, s = 1, 2

p(0, 0, '8', w)
p(4, 4, '8', w)
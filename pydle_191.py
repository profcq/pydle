t = ''
p, r = pydle, range

for x in r(2):
    for y in r(0, 5, 2):
        p(x, y, '', 'white')

for x in r(2, 5, 2):
    for y in r(5):
        p(x, y, t, 'red')

    t = '⚫'
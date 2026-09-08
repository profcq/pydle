b, c, t = ['00', '10', '20', '21'], 0, ['M', 'OU', 'SE', '©', '19', '83']
p, r, r5 = pydle, range, range(5)

for x in r5:
    for y in r5:
        if not f'{x}{y}' in b:
            p(x, y, '', 'white')

for x in r(1, 4, 2):
    p(x, 2, '', 'green')

p(2, 2, 'MS', 'yellow')

for y in r(3, 5):
    for x in r(1, 4):
        p(x, y, f'{t[c]}', 'yellow')
        c += 1
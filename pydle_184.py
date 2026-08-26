p = ['30', '31', '41', '22', '03', '13', '14']
r = range

for x in r(5):
    for y in r(5):
        if not f'{x}{y}' in p:
            pydle(x, y, '', 'white')
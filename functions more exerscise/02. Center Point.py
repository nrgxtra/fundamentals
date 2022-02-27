

def coord(a, b, c, d):
    j = abs(a) + abs(b)
    k = abs(c) + abs(d)
    if j <= k:
        return f'({int(a)}, {int(b)})'
    elif k < j:
        return f'({int(c)}, {int(d)})'


print(coord(float(input()), float(input()), float(input()), float(input())))


def longer_line(a, b, c, d, e, f, g, h):
    l1 = abs(abs(a - c) + abs(b - d))
    l2 = abs(abs(e - g) + abs(f - h))
    if l1 >= l2:
        if abs(a + b) <= abs(c + d):
            return f'({int(a)}, {int(b)})({int(c)}, {int(d)})'
        else:
            return f'({int(c)}, {int(d)})({int(a)}, {int(b)})'
    else:
        if abs(e + f) <= abs(g + h):
            return f'({int(e)}, {int(f)})({int(g)}, {int(h)})'
        else:
            return f'({int(g)}, {int(h)})({int(e)}, {int(f)})'


print(longer_line(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()),
                  float(input()), float(input())))

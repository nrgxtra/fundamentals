def mult(a, b, c):
    negative = False
    if a < 0 and b > 0 and c > 0:
        negative = True
    if a > 0 and b < 0 and c > 0:
        negative = True
    if a > 0 and b > 0 and c < 0:
        negative = True
    if a < 0 and b < 0 and c < 0:
        negative = True
    if negative:
        return 'negative'

    elif a == 0 or b == 0 or c == 0:
        return 'zero'
    elif not negative:
        return 'positive'


print(mult(float(input()), float(input()), float(input())))

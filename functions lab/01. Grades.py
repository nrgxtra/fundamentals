t = ('Fail', 'Poor', 'Good', 'Very Good', 'Excellent')


def gr(grade):
    if 2.00 <= grade <= 2.99:
        return t[0]
    if 3.00 <= grade <= 3.49:
        return t[1]
    if 4.00 <= grade <= 4.49:
        return t[2]
    if 4.50 <= grade <= 5.49:
        return t[3]
    if 5.50 <= grade <= 6.00:
        return t[4]


print(gr(float(input())))


n = int(input())
n1 = int(input())


def fact(a, b):
    f1 = a
    f2 = b
    for i in range(a - 1, 0, -1):
        f1 *= i
    for j in range(b - 1, 0, -1):
        f2 *= j
    result = f1 / f2
    return f'{result:.2f}'


print(fact(n, n1))

ops = ('multiply', 'divide', 'add', 'subtract')


def calc(op, a, b):
    if op in ops:
        if op == 'multiply':
            return a * b
        elif op == 'divide':
            return int(a / b)
        elif op == 'add':
            return a + b
        elif op == 'subtract':
            return a - b


print(calc(input(), int(input()), int(input())))

t = ('coffee', 'coke', 'water', 'snacks')


def calc(item, num):
    if item == 'coffee':
        return 1.50 * num
    elif item == 'coke':
        return 1.4 * num
    elif item == 'water':
        return 1.00 * num
    elif item == 'snacks':
        return 2 * num


print(f'{calc(input(), int(input())):.2f}')

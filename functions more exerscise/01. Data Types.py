
def data_type(a, b):
    if a == 'int':
        return int(b) * 2
    elif a == 'real':
        return f'{(float(b) * 1.5):.2f}'
    elif a == 'string':
        return f'${b}$'


print(data_type(input(), input()))



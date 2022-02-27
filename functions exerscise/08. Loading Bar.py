n = int(input())


def loading(a):
    empty = ''
    for i in range(1, a, 10):
        empty += '%'
    for j in range(a, 100, 10):
        empty += '.'
    if a < 100:
        print(f'{a}% [{empty}]')
        print('Still loading...')
    else:
        print('100% Complete!')
        print('[%%%%%%%%%%]')


loading(n)

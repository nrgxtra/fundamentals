num = float(input())
if num == 0:
    print('zero')
elif num > 0:
    if abs(num) > 1000000:
        print('large positive')
    elif abs(num) < 1:
        print('small positive')
    else:
        print('positive')
else:
    if abs(num) > 1000000:
        print('large negative')
    elif abs(num) < 1:
        print('small negative')
    else:
        print('negative')

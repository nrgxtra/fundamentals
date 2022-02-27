n = int(input())

for i in range(1, n + 1):
    sum_of_digits = 0
    num = i
    while num > 0:
        sum_of_digits += num % 10
        num = int(num / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')


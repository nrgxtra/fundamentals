n = int(input())

for i in range(1, n + 1):
    sum_of_digits = 0

    for cd in range(len(str(i))):
        sum_of_digits += int(str(i)[cd])
    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

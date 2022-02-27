n = input()


def odd_even(a):
    odd = 0
    even = 0
    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            even += int(a[i])
        else:
            odd += int(a[i])
    return (f'Odd sum = {odd}, Even sum = {even}')


print(odd_even(n))

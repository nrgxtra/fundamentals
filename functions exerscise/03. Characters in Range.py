first_ch = input()
second_ch = input()


def between(a, b):
    result = ''
    for i in range(ord(first_ch) + 1, ord(second_ch)):
        result += chr(i) + ' '
    return result


print(between(first_ch, second_ch))

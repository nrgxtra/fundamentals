import re

pattern = r'^(%?\$?)([A-Z]{1}[a-z]{2}[a-z]*)\1: ((\[[0-9]+\]\|){3})$'
n = int(input())
for i in range(n):
    message = input()
    result = re.findall(pattern, message)
    if len(result) == 0:
        print("Valid message not found!")
    else:
        matches = re.finditer(pattern, message)
        for match in matches:
            x = match.group(3)
            x = x.replace(']|[', ' ')
            x = x.replace('[', ' ')
            x = x.replace(']|', '')
            z = x.split(' ')
            k = [int(p) for p in z if p != '']
            second_part = ''
            b = [chr(g) for g in k]
            for w in range(len(b)):
                second_part += b[w]
            print(f'{match.group(2)}: ', end='')
            print(second_part)

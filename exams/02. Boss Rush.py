import re

n = int(input())
pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#'
for i in range(n):
    boss = input()
    valid = re.findall(pattern, boss)
    if len(valid) > 0:
        matches = re.finditer(pattern, boss)
        for match in matches:
            print(f'{match.group(1)}, The {match.group(2)}')
            print(f'>> Strength: {len(match.group(1))}')
            print(f'>> Armour: {len(match.group(2))}')
    else:
        print('Access denied!')

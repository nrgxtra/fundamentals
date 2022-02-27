mine = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in mine:
        mine[resource] = 0
    mine[resource] += quantity
[print(f'{r} -> {q}') for (r, q) in mine.items()]

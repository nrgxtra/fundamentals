quantity = int(input())
days = int(input())
spending = 0
christmas_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        spending += 2 * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        spending += 8 * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        spending += 15 * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        spending += 23
    if day % 10 == 0 and day == days:
        christmas_spirit -= 30
print(f'Total cost: {spending}')
print(f'Total spirit: {christmas_spirit}')


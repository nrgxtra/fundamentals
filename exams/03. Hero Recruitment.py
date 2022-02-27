heroes = dict()
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(' ')
    action = tokens[0]
    if action == 'Enroll':
        hero = tokens[1]
        if hero not in heroes:
            heroes[hero] = []
        else:
            print(f'{hero} is already enrolled.')
    elif action == 'Learn':
        hero = tokens[1]
        spell = tokens[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        else:
            if spell in heroes[hero]:
                print(f"{hero} has already learnt {spell}.")
            else:
                heroes[hero].append(spell)
    elif action == 'Unlearn':
        hero = tokens[1]
        spell = tokens[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        else:
            if spell not in heroes[hero]:
                print(f"{hero} doesn't know {spell}.")
            else:
                idx = heroes[hero].index(spell)
                heroes[hero].pop(idx)
sort_heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))
print('Heroes:')
for hero, spell in sort_heroes.items():
    print(f"== {hero}: {', '.join(spell)}")



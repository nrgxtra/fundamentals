legendary = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
winner = ''
while winner == '':
    tokens = input().lower().split(' ')
    for index in range(0, len(tokens), 2):
        item = tokens[index + 1]
        quantity = int(tokens[index])
        if item in legendary:
            legendary[item] += quantity
            if legendary[item] >= 250:
                winner = item
                break
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity

if winner == 'shards':
    print('Shadowmourne obtained!')
    legendary['shards'] -= 250
elif winner == 'fragments':
    legendary['fragments'] -= 250
    print('Valanyr obtained!')
elif winner == 'motes':
    print('Dragonwrath obtained!')
    legendary['motes'] -= 250
legendary = dict(sorted(legendary.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items()))
for (l, m) in legendary.items():
    print(f'{l}: {m}')
for (p, q) in junk.items():
    print(f'{p}: {q}')

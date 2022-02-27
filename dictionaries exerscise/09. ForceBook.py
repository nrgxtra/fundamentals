sides = dict()
while True:
    input_lines = input()
    if input_lines == 'Lumpawaroo':
        break
    tokens = input_lines.split(' | ')
    if len(tokens) == 2:
        (side, user) = tokens
        contained = False
        for key, value in sides.items():
            if user in value:
                contained = True
                break
        if not contained:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)
    else:
        tokens = input_lines.split(' -> ')
        (user, side) = tokens
        for key, value in sides.items():
            if user in value:
                sides[key].remove(user)
                break
        if side not in sides:
            sides[side] = []
        sides[side].append(user)
        print(f"{user} joins the {side} side!")
sorted_sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in sorted_sides.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        [print(f'! {name}') for name in sorted(value)]

zoo = dict()

while True:
    com = input()
    if com == 'Last Info':
        break
    else:
        tokens = com.split(':')
        command = tokens[0]
        if command == 'Add':
            name = tokens[1]
            food_limit = int(tokens[2])
            area = tokens[3]
            if area not in zoo:
                zoo[area] = [[name, food_limit]]
            elif area in zoo and name not in zoo[area][0]:
                zoo[area].append([name, food_limit])
            else:
                zoo[area][0][1] += food_limit
        elif command == 'Feed':
            name = tokens[1]
            food = int(tokens[2])
            area = tokens[3]
            if name in zoo[area][0]:
                zoo[area][0][1] -= food
                if zoo[area][0][1] <= 0:
                    print(f'{name} was successfully fed')
                    del zoo[area][0][1]
                    del zoo[area][0]
            if not zoo[area] :
                del zoo[area]

print('Animals:')
sortedll = []
for k, v in zoo.items():
    sortedll.append(v)
print(sortedll)


for el in sortedll:
    print(el)
    print(f'{el[0][1]} -> {el[1]}g')
print('Areas with hungry animals:')
for area, animals in zoo.items():
    print(f'{area} : {len(animals)}')


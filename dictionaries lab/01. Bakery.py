line = input().split(' ')
bakery = {line[i]: int(line[i+1]) for i in range(0, len(line), 2)}
print(bakery)


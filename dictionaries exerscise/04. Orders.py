price_dd = dict()
quantity_dd = dict()
while True:
    command = input()
    if command == 'buy':
        break
    tokens = command.split(' ')
    name = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    if name not in price_dd:
        price_dd[name] = 0
    price_dd[name] = price
    if name not in quantity_dd:
        quantity_dd[name] = 0
    quantity_dd[name] += quantity
total = {name: price_dd[name]*quantity_dd[name] for name in price_dd and quantity_dd}
for i, j in total.items():
    print(f'{i} -> {j:.2f}')

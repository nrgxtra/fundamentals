stats = []

while True:
    com = input()
    if com == 'statistics':
        break
    stats.append(com)
statistics = {}
for prod in stats:
    (product, quantity) = prod.split(': ')
    if product in statistics:
        statistics[product] += int(quantity)
    else:
        statistics[product] = int(quantity)
print("Products in stock:")
for (product, quantity) in statistics.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(statistics)}')
print(f'Total Quantity: {sum(statistics.values())}')


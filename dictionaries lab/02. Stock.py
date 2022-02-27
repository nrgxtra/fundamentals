line = input().split(' ')
searched = input().split(' ')
prod_dd = {line[i]: int(line[i+1]) for i in range(0, len(line), 2)}

for product in searched:
    if product in prod_dd:
        quantity = prod_dd[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


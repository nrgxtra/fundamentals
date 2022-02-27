budget = float(input())
floor_price = float(input())
egg_price = floor_price * 0.75
milk_price = floor_price * 1.25
cosunac_price = egg_price + floor_price + milk_price / 4
current_spending = 0
cosunac_counter = 0
colored_egg_counter = 0

while current_spending < budget:
    current_spending += cosunac_price
    if current_spending > budget:
        current_spending -= cosunac_price
        break
    cosunac_counter += 1
    colored_egg_counter += 3
    if cosunac_counter % 3 == 0:
        colored_egg_counter -= (cosunac_counter - 2)
balance = budget - current_spending
print(f'You made {cosunac_counter} cozonacs! Now you have {colored_egg_counter} eggs and {balance:.2f}BGN left.')

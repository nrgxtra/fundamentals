
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_repair_count = 0
total_cost = 0
for i in range(1, lost_fights+1):
    if i % 2 == 0:
        total_cost += helmet_price
    if i % 3 == 0:
        total_cost += sword_price
    if i % 2 == 0 and i % 3 == 0:
        total_cost += shield_price
        shield_repair_count += 1
    if shield_repair_count == 2:
        total_cost += armor_price
        shield_repair_count = 0
print(f'Gladiator expenses: {total_cost:.2f} aureus')

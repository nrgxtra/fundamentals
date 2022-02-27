guests = {}
unlikes = 0

while True:
    command = input()
    if command == "Stop":
        break
    tokens = command.split("-")
    action = tokens[0]
    if action == "Like":
        guest = tokens[1]
        meal = tokens[2]
        if guest not in guests.keys():
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)
    elif action == "Unlike":
        guest = tokens[1]
        meal = tokens[2]
        if guest not in guests.keys():
            print(f"{guest} is not at the party.")
        elif meal not in guests[guest]:
            print(f"{guest} doesn`t have the {meal} in his/her collection.")
        else:
            guests[guest].remove(meal)
            unlikes += 1
            print(f"{guest} doesn`t like the {meal}.")

ordered = dict(sorted(guests.items(), key=lambda x: (-x[1], x[0])))
for key, value in ordered.items():
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {unlikes}")





friends_list = input().split(', ')
blacklisted = 0
lost = 0
while True:
    command = input()
    if command == 'Report':
        break
    tokens = command.split(' ')
    s_com = tokens[0]
    if s_com == 'Blacklist':
        name = tokens[1]
        if name not in friends_list:
            print(f"{name} was not found.")
        else:
            print(f"{name} was blacklisted.")
            friends_list = ['Blacklisted' if x == name else x for x in friends_list]
            blacklisted += 1
    elif s_com == 'Error':
        index = int(tokens[1])
        name = friends_list[index]
        if name == 'Blacklisted' or name == 'Lost':
            continue
        else:
            print(f"{name} was lost due to an error.")
            friends_list = ['Lost' if x == name else x for x in friends_list]
            lost += 1
    elif s_com == 'Change':
        index = int(tokens[1])
        if 0 <= index < len(friends_list):
            name = friends_list[index]
            new_name = tokens[2]
            print(f"{name} changed his username to {new_name}.")
            friends_list = [new_name if x == name else x for x in friends_list]
        else:
            continue

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(' '.join(friends_list))

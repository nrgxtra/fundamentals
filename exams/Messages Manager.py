users_base = dict()
capacity = int(input())
while True:
    command = input()
    if command == 'Statistics':
        break
    tokens = command.split('=')
    com = tokens[0]
    if com == 'Add':
        username = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])
        if username not in users_base:
            users_base[username] = [sent, received]
    elif com == 'Message':
        sender = tokens[1]
        receiver = tokens[2]
        if sender and receiver in users_base:
            x = users_base[sender].pop(0)
            users_base[sender].insert(0, x+1)
            if users_base[sender][0]+users_base[sender][1] >= capacity:
                users_base.pop(sender)
                print(f"{sender} reached the capacity!")
            y = users_base[receiver].pop(1)
            users_base[receiver].insert(1, y+1)
            if users_base[receiver][1] + users_base[receiver][0] >= capacity:
                users_base.pop(receiver)
                print(f"{receiver} reached the capacity!")
    elif com == 'Empty':
        username = tokens[1]
        if username == 'All':
            users_base.clear()
        if username in users_base:
            users_base.pop(username)
print(f'Users count: {len(users_base)}')
sort_base = dict(sorted(users_base.items(), key=lambda x: (-x[1][1], x[0])))
for user, msg in sort_base.items():
    print(f'{user} - {msg[0]+msg[1]}')



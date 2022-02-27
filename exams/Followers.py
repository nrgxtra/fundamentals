user_base = dict()
while True:
    command = input()
    if command == 'Log out':
        break
    tokens = command.split(':')
    action = tokens[0]
    if action == 'New follower':
        username = tokens[1]
        if username not in user_base:
            user_base[username] = [0, 0]
    elif action == 'Like':
        username = tokens[1]
        count = int(tokens[2])
        if username not in user_base:
            user_base[username] = [count, 0]
        else:
            user_base[username][0] += count
    elif action == 'Comment':
        username = tokens[1]
        if username not in user_base:
            user_base[username] = [0, 1]
        else:
            user_base[username][1] += 1
    elif action == 'Blocked':
        username = tokens[1]
        if username in user_base:
            user_base.pop(username)
        else:
            print(f"{username} doesn't exist.")
print(f'{len(user_base)} followers')
sort_base = dict(sorted(user_base.items(), key=lambda x: (-x[1][0], x[0])))
for user, likes in sort_base.items():
    print(f'{user}: {likes[0]+likes[1]}')

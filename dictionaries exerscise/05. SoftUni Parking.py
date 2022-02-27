n = int(input())
registered_users = dict()
for i in range(n):
    command = input()
    tokens = command.split(' ')
    action = tokens[0]
    if action == 'register':
        username = tokens[1]
        licence_plate = tokens[2]
        if username not in registered_users:
            registered_users[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_users[username]}")
    elif action == 'unregister':
        username = tokens[1]
        if username not in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_users.pop(username)
for users, plates in registered_users.items():
    print(f"{users} => {plates}")

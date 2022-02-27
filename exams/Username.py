username = input()
while True:
    command = input()
    if command == 'Sign up':
        break
    tokens = command.split(' ')
    action = tokens[0]
    if action == 'Case':
        what = tokens[1]
        if what == 'lower':
            username = username.lower()
        elif what == 'upper':
            username = username.upper()
        print(username)
    elif action == 'Reverse':
        start = int(tokens[1])
        end = int(tokens[2])
        if 0 <= start < len(username) and 0 <= end < len(username):
            new_user = reversed(username[start:end+1])
            print(''.join(new_user))
    elif action == 'Cut':
        substring = tokens[1]
        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
        else:
            username = username.replace(substring, '')
            print(username)
    elif action == 'Replace':
        char = tokens[1]
        username = ''.join(['*' if x == char else x for x in username])
        print(username)
    elif action == 'Check':
        char = tokens[1]
        if char in username:
            print('Valid')
        else:
            print(f"Your username must contain {char}.")

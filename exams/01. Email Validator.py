
email = input()

while True:
    command = input()
    tokens = command.split(' ')

    if command == 'Complete':
        break
    elif command == 'Make Upper':
        email = email.upper()
        print(email)
    elif command == 'Make Lower':
        email = email.lower()
        print(email)
    elif 'GetDomain' in command:
        count = int(tokens[1])
        print(email[-count:])
    elif command == 'GetUsername':
        if '@' in email:
            for j in range(len(email)):
                if email[j] == '@':
                    break
                else:
                    print(email[j], end='')
            print()
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif 'Replace' in command:
        char = tokens[1]
        for h in range(len(email)):
            if email[h] == char:
                print('-', end='')
            else:
                print(email[h], end='')
        print()
    elif command == 'Encrypt':
        encrypted = ''
        for i in range(len(email)):
            encrypted += str((ord(email[i]))) + ' '
        print(encrypted)


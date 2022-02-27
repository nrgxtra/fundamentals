users = dict()
languages = dict()

while True:
    command = input()
    if command == 'exam finished':
        break
    tokens = command.split('-')
    if len(tokens) == 2:
        username = tokens[0]
        if username in users:
            users.pop(username)
    else:
        username = tokens[0]
        language = tokens[1]
        points = int(tokens[2])
        if username not in users:
            users[username] = 0
        if users[username] < points:
            users[username] = points
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
ordered_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
ordered_languages = dict(sorted(languages.items()))
print('Results:')
for users, points in ordered_users.items():
    print(f'{users} | {points}')
print('Submissions:')
for lang, times in ordered_languages.items():
    print(f'{lang} - {times}')

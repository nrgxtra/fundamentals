courses = dict()
while True:
    command = input()
    if command == 'end':
        break
    tokens = command.split(' : ')
    course = tokens[0]
    student = tokens[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for i, j in courses.items():
    print(f'{i}: {len(j)}')
    for k, h in courses.items():
        if k == i:
            [print(f"-- {item}") for item in sorted(j)]






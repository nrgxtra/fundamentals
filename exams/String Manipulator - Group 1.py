string = input()
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(' ')
    if tokens[0] == 'Translate':
        char = tokens[1]
        replacement = tokens[2]
        string = string.replace(char, replacement)
        print(string)
    elif tokens[0] == 'Includes':
        string1 = tokens[1]
        included = False
        if string1 in string:
            included = True
        print(included)
    elif tokens[0] == 'Start':
        string1 = tokens[1]
        starts = False
        if string1 in string:
            starts = True
        print(starts)
    elif tokens[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif tokens[0] == 'FindIndex':
        char = tokens[1]
        idx = 0
        for i in range(len(string)):
            if string[i] == char and i > idx:
                idx = i
        print(idx)
    elif tokens[0] == 'Remove':
        start_idx = int(tokens[1])
        count = int(tokens[2])
        string1 = ''
        for j in range(len(string)):
            if j < start_idx or j >= start_idx + count:
                string1 += string[j]
        print(string1)

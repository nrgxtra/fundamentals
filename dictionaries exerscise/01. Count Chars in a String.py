strings = input().split(' ')
string = ''.join(strings)
letters = {}
for item in string:
    if item not in letters:
        letters[item] = 0
    letters[item] += 1
[print(f'{letter} -> {count}') for (letter, count) in letters.items()]

first_string = input()
second_string = input()
previous = first_string
for ind in range(len(first_string)):
    new_string = ''
    for i in range(0, ind + 1):
        new_char = second_string[i]
        new_string += new_char
    for j in range(ind + 1, len(first_string)):
        new_char2 = first_string[j]
        new_string += new_char2
    if new_string != previous:
        print(new_string)
        previous = new_string


skill = input()
while True:
    command = input()
    if command == 'For Azeroth' or command is None:
        break
    if command == 'GladiatorStance':
        skill = skill.upper()
        print(skill)
    elif command == 'DefensiveStance':
        skill = skill.lower()
        print(skill)
    elif command.split(' ')[0] == 'Dispel' and len(command.split(' ')) == 3:
        index = int(command.split(' ')[1])
        letter = command.split(' ')[2]
        if 0 <= index < len(skill):
            skill = skill.replace(skill[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command.split(' ')[0] == 'Target' and command.split(' ')[1] == 'Change' and len(command.split(' ')) == 4:
        substring = command.split(' ')[2]
        second = command.split(' ')[3]
        skill = skill.replace(substring, second)
        print(skill)
    elif command.split(' ')[0] == 'Target' and command.split(' ')[1] == 'Remove' and len(command.split(' ')) == 3:
        sbstr = command.split(' ')[2]
        skill = skill.replace(sbstr, '')
        print(skill)
    else:
        print("Command doesn't exist!")

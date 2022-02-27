import re

pattern = r'(.+)[<->]([0-9]{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})[<->]\1'
n = int(input())
for i in range(n):
    username = input()
    valid = re.findall(pattern, username)
    if len(valid) == 0:
        print("Try another password!")
    else:
        password = re.finditer(pattern, username)
        for mach in password:
            encrypted = ''.join(mach.group(2))
            encrypted_good = ''.join([x for x in encrypted if x != '|'])
            print(f'Password: {encrypted_good}')

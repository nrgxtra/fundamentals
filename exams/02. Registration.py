n = int(input())
success_count = 0
for r in range(n):
    reg = input()
    end_user = ''
    end_pass = ''
    legit_name = False
    name_ok = False
    name_t = reg.split("P@$")
    full_name = list(name_t[0])
    if full_name[0] == 'U' and full_name[1] == '$' and full_name[-1] == '$' and full_name[-2] == 'U':
        legit_name = True
    if legit_name:
        username = full_name[2:-2]
        legit_u = False
        if len(username) >= 3 and ord(username[0]) in range(65, 91):
            res = [x for x in username if ord(x) in range(97, 123)]
            if len(res) == len(username) - 1:
                legit_u = True
            if legit_u:
                name_ok = True
                end_user = ''.join(username)
        else:
            print("Invalid username or password")
            continue
    else:
        print("Invalid username or password")
        continue
    password_t = reg.split('U$')
    full_pass = list(password_t[2])
    legit_pass = False
    pass_ok = False
    if full_pass[0] == 'P' and full_pass[1] == '@' and full_pass[2] == '$' and full_pass[-1] == '$' and full_pass[-2] == '@' and full_pass[-3] == 'P':
        legit_pass = True
    if legit_pass:
        password = full_pass[3:-3]
        pass_code = [x for x in password[:5] if x.isalpha]
        last_dig = password[-1]
        if len(pass_code) >= 5 and ord(last_dig) in range(48, 58):
            pass_ok = True
            end_pass = ''.join(password)
    else:
        print("Invalid username or password")
        continue
    if name_ok and pass_ok:
        print("Registration was successful")
        print(f"Username: {end_user}, Password: {end_pass}")
        success_count += 1
    else:
        print("Invalid username or password")
print(f"Successful registrations: {success_count}")

password = input()


def validator(a):
    valid_num = False
    valid_len = False
    valid_content = False
    if 6 <= len(a) <= 10:
        valid_len = True
    else:
        print("Password must be between 6 and 10 characters")
    digits = 0
    content = False
    valid_count = 0
    for i in range(len(a)):
        if 48 <= ord(a[i]) <= 57:
            digits += 1
        if (48 <= ord(a[i]) <= 57) or (65 <= ord(a[i]) <= 90) or (97 <= ord(a[i]) <= 122):
            valid_count += 1
        else:
            valid_content = False
            content = True
    if content:
        print("Password must consist only of letters and digits")
    if valid_count == len(a):
        valid_content = True

    if digits >= 2:
        valid_num = True
    else:
        print("Password must have at least 2 digits")
    if valid_content and valid_num and valid_len:
        print("Password is valid")


validator(password)

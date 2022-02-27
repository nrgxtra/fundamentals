start_year = int(input())
current_year = start_year + 1
found = False
while True:
    not_found = False
    for fi in range(len(str(current_year))):
        for si in range(fi + 1, len(str(current_year))):
            fd = str(current_year)[fi]
            sd = str(current_year)[si]
            if fd == sd:
                not_found = True
                break
    if not_found:
        current_year += 1
    else:
        found = True
        break
if found:
    print(current_year)




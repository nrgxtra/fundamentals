
owned_tanks = input().split(', ')
n = int(input())

for i in range(n):
    command = input().split(', ')
    sc = command[0]
    if sc == 'Add':
        name = command[1]
        if name in owned_tanks:
            print("Tank is already bought")
        else:
            print("Tank successfully bought")
            owned_tanks.append(name)
    elif sc == 'Remove':
        name = command[1]
        if name in owned_tanks:
            print("Tank successfully sold")
            owned_tanks = [x for x in owned_tanks if x != name]
        else:
            print("Tank not found")
    elif sc == 'Remove At':
        idx = int(command[1])
        if 0 <= idx < len(owned_tanks):
            print("Tank successfully sold")
            del owned_tanks[idx]
        else:
            print("Index out of range")
    elif sc == 'Insert':
        idx = int(command[1])
        name = command[2]
        if idx < 0 or idx > len(owned_tanks)-1:
            print("Index out of range")
        else:
            if name in owned_tanks:
                print("Tank is already bought")
            else:
                owned_tanks.insert(idx, name)
                print("Tank successfully bought")

print(', '.join(owned_tanks))



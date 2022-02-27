num = int(input())

for i in range(1, num+1):
    for j in range(1, i+1):
        print('*', end='')
    print()
for h in range(num, 1, -1):
    for k in range(h, 1, -1):
        print('*', end='')
    print()

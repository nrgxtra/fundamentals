
n = int(input())

for i in range(n):
    for j in range(n):
        for h in range(n):
            print(f'{chr(97+i)}{chr(97+j)}{chr(97+h)}')

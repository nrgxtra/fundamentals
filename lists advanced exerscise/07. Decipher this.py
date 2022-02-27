
words = input().split(' ')
result = ''

for word in words:
    fch = [j for j in word if j.isdigit()]
    chr_left = [j for j in word if j.isalpha()]
    chr_left[0], chr_left[-1] = chr_left[-1], chr_left[0]
    result += chr(int(''.join(fch)))
    result += ''.join(chr_left) + ' '
print(result)



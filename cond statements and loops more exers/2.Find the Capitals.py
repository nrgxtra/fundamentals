word = input()
ll = []

for cl in range(len(word)):
    if (word[cl] >= 'A') and (word[cl] <= 'Z'):
        ll += [cl]
print(ll)

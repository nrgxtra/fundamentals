n = int(input())
dd = {}
for i in range(n):
    word = input()
    synonyms = input()
    if word not in dd:
        dd[word] = []

    dd[word].append(synonyms)

for (word, synonym) in dd.items():
    print(f"{word} - {', '.join(synonym)}")

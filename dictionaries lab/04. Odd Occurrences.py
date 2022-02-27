words = input()
word_str = [word.lower() for word in words.split(' ')]
for_chk = {}
for word1 in word_str:
    if word1 not in for_chk:
        for_chk[word1] = 1
    else:
        for_chk[word1] += 1

odd_words = [word for (word, count) in for_chk.items() if count % 2 == 1]
print(' '.join(odd_words))

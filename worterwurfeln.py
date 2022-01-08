import sys
import unidecode

#filename = "ThirdParty/words/Words/fr.txt"
filename = "ThirdParty/words/Words/en.txt"
letters = ['n', 'e', 'n', 'r', 'h', 's', 'u', 'r', 'h', 'y', 'd', 'i', 'g']

words = []
with open(filename) as file:
    for line in file:
        word = line.rstrip().lower()
        word = unidecode.unidecode(word)
        words.append(word)

letters_dict = {}
for letter in letters:
    letters_dict[letter] = letters_dict.get(letter, 0) + 1

best_words = []
for word in words:
    word_dict = {}
    for letter in word:
        word_dict[letter] = word_dict.get(letter, 0) + 1

    found = True
    for letter, count in word_dict.items():
        if not (letter in letters_dict):
            found = False
            break
        if letters_dict[letter] < count:
            found = False
            break

    if found:
        best_words.append(word)

best_words.sort(key=len, reverse=True)
for i in range(min(10, len(best_words))):
    print(best_words[i])


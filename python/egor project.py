import sys
import string

with open("words.txt", 'r') as file:
    file = file.read()
    dictionary = set(file.split("\n"))

with open("reverse.txt", 'r') as file:
    sentence = file.read().split()

translator = str.maketrans("", "", string.punctuation.replace("-", ""))
sentence = [word.translate(translator) for word in sentence]

for word in sentence:
    org_word = word
    if word.isnumeric():
        continue
    if word[0].isupper():
        continue
    if "'s" in word:
        word = word.split("'s")[0]

    if word.endswith("ing"):
        word = word.removesuffix("ing")
        if word[-1] == word[-2]:
            word = word[:-1]
        elif not word.endswith("y"):
            word += "e"

    if word not in dictionary:
        if word.endswith("ies"):
            word = word.replace("ies", "y")
        word = word.removesuffix("s")
        word = word.removesuffix("e")
        if word not in dictionary:
            print("misspelled word: ", org_word)


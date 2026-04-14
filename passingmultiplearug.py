dict_words = {
    "Hi": "Halo",
    "Who": "Tun",
    "Are": "Apa",
    "You": "Kon"
}

def translate(sentence):
    words = sentence.split()
    result = []

    for word in words:
        word_cap = word.capitalize()

        if word_cap in dict_words:
            result.append(dict_words[word_cap])
        else:
            result.append(word)

    return " ".join(result)

# function call
print(translate("Hi Who are You"))
dict_words = {
    "Hi": "Halo",
    "Who": "Tun",
    "Are": "",
    "You":"Kon"
}

def calculateTotalSum(sentence):
    words = sentence.split()  
    
    for word in words:
        # if (word.islower()):
        word = word.capitalize()  

        if word in dict_words:
            print(dict_words[word])
        else:
            print(word)  
# function call
calculateTotalSum("Hi Who are You")
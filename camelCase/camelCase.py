# Algorithm, wich who write in camel case

def camelCaseFunction(text):
    caps=0
    word1=""
    word2=""
    with open('camelCase\motlettres.txt', 'r') as f :
        words = [elt.split(" ") for elt in f ]
        for letter in text:
            if caps==0:
                word1 += letter
                for word in words[0] :
                    if word1 == word.lower() :
                        caps=1
            else:
                word2+=letter

    return word1+word2.capitalize()

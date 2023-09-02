# Reverse string
# Reverse words only with 5 or more letters


def spin_words(sentence):
    reverse = []
    word_list = sentence.split()
    for a in word_list:
        if len(a) >= 5:
            reverse.append(a[::-1])
        else:
            reverse.append(a)
    return reverse

print(spin_words("I love you Krishia Ocampo"))
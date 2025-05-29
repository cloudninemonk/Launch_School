def titlize(sentence):
    words = sentence.split()
    # print(words)
    new_words = []

    for word in words:
        if len(word) > 2:
            # print(len(word))
            word = word.capitalize()
        new_words.append(word)


    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
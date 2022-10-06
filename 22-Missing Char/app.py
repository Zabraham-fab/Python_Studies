def missing_char(word, n):
    new_word = ""
    if n not in list(range(0,len(word))):
        return "Word out of index"
    for i in word:
        if i == word[n]:
            continue
        elif i != word[n]:
            new_word += i
    return new_word
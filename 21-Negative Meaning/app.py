def not_string(word):
    if word.startswith("not"):
        return word
    else:
        return "not"+" "+word
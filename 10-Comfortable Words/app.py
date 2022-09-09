right = list("QWERTASDFGZXCVBqwertasdfgzxcvb")
left = list("YUIOPĞÜHJKLŞİNMÖÇyuıopğühjklşinmöç")
tupr = set(right)
tupl = set(left)
word = input('Enter a word to see if the word you entered is comfortable:')
#word = "clarusway"
x = set(word)
if x.intersection(tupr) == x:
     print("False")
elif x.intersection(tupl) == x:
    print("False")
else:
    print("True")
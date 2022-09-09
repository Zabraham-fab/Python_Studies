numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
a=list(set(numbers))
b = []
for i in range(len(a)):
    #print(a[i],'=',numbers.count(a[i]))
    b.insert(i,numbers.count(a[i]))
k = max(b)
c = b.index(max(b))
d = a[c]
print("numbers list" , numbers,"the most freaquant number", d, end=', ')
print("it was repeated", k, "times.")

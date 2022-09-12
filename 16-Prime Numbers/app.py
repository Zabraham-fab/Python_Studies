n = int(input("Please enter you number for find all prime number until the number you entered: "))
P = []
for num in range((n+1)):
    if num==2 or num==3 or num==5 or num==7:
        P.append(num)
    elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
        continue
    elif num%num==0:
        P.append(num)
print(P)
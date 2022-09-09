while True:
    ams = input("Enter your number for finding n-Amstrong number.")
    if ams.isnumeric() == True:
        cont = list(ams)
        print(cont)
        po = len(cont)
        sum = 0
        for i in cont:
            amg = int(i)**(int(po))
            sum += amg
        print(f"'{ams}' Armstrong number sumary is '{sum}'")
        break
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
     
sum_list = list(str(sum))
if sum_list == cont:
    print(f"'{ams}' number is Armstrong number.")
else:
    print(f"'{ams}' number is not Armstrong number.")
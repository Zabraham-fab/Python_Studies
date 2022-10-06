F_B = []
for num in range(0,100):
    if num!=0 and num%3==0:
        F_B.insert(num,"Fizz")
        print(F_B[num])
        if num!=0 and num%3==0 and num%5==0:
            F_B.pop(num)
            F_B.insert(num,"FizzBuzz")
            print(F_B[num])
    elif num!=0 and num%5==0:
        F_B.insert(num,"Buzz")
        print(F_B[num])
    else:
        F_B.append(num)
        print(F_B[num])
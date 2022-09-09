num = int(input("Please enter your a number for learning whether your written number is prime number.: "))  
if num==2 or num==3 or num==5 or num==7:
    print(f"{num} is a prime number.")
elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
    print(f"{num} is not a prime number.")
elif num%num==0:
    print(f"{num} is a prime number.")
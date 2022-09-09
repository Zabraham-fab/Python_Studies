age = input('Are you a cigarette addict older than 75 years old?(True/False) : ').capitalize()
chronic = (input('Do you have a severe chronic disease?(True/False) :').capitalize())
immune =(input('Is your immune system too weak?(True/False) :').capitalize())

age = True if "True" in age else False
chronic = True if "True" in chronic else False
immune = True if "True" in immune else False

result = age or chronic or immune

if result == True:
    print("You are in risky group")
elif result == False:
    print("You are not in risky group")
def parrot_trouble(talking, hour) :
    if talking == True:
        if hour in list(range(6,22)) :
            return False
        else:
            return True
    elif talking == False :
        return False
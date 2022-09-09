year = int(input('Enter a 4-digit year to find the leap year: '))
a_y = (year % 400)
print('It is not leap year your entering year:{}'.format(a_y==0 and 1))
number = input('Enter a number: ')

try:
    print(int(number))
except:
    print('input must be numeric')
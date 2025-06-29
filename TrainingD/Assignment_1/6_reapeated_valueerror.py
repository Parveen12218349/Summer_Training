
while(True):
    number = input('Enter a number: ')
    try:
        convert_numeric = int(number)
        print(convert_numeric)
        break
    except:
        print('Enter a numeric value')
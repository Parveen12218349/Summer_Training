"""

Date: 19-6-2030
Author: Parveen
Description:  Simple menu driven calculator

"""

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
user_choice = (input('1. Add 2. Sub 3. Mul'))

"""

if user_choice == 1:
    print(f'Sum: {num1 + num2}')
elif user_choice == 2:
    print(f'Diff: {num1 - num2}')
elif user_choice == 3:
    print(f'Product: {num1 * num2}')
    
"""


match user_choice:
    case '1':
        print(f'Sum: {num1 + num2}')
    case '2':
        print(f'Diff: {num1 - num2}')
    case '3':
        print(f'Product: {num1 * num2}')
    case _:
        print('Enter 1-3')


print('Process finished with exit code 0')
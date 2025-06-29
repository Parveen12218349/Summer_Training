"""

Date: 19-6-2030
Author: Parveen
Description:  Armstrong number

"""

user_value = int(input('Enter a number: '))
orig = user_value

sum = 0
while user_value > 0:
    rem = user_value % 10
    sum = sum + (rem ** 3)
    user_value = user_value // 10

if sum == orig:
    print('Armstrong number')
else:
    print('Not an armstrong number')
from  string_utils.string_operations import reverse_string,upper_string,str_length
from string_utils.string_validation import palindrome_string,alphabet_only

str = input('Enter a string: ')
print('Function_usage of string_operation\n')
print(f'reverse of {str} is: {reverse_string(str)}')
print(f' uppercase of {str} is: {upper_string(str)}')
print(f'length of {str} is: {str_length(str)}\n')

print('Function_usage of string_validation\n')
if(palindrome_string(str)):
    print(f'{str} is a palindrome string')
else:
    print(f'{str} is not a palindrome string')

if(alphabet_only(str)):
    print(f'{str} contains only alphabets')
else:
    print(f"{str} doesn't contains only alphabets")
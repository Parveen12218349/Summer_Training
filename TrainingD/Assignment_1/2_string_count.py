vowels = 'aeiouAEIOU'
consonents = 'bcdfghjklmnpqustvwxyzBCDFGHJKLMNPQRSTVWXYZ'
string_input = input("Enter a string: ")
count_vowel=0
count_consonent=0

string_input_list = list(string_input)
for i in range(len(string_input_list)):
    if(string_input_list[i] in vowels):
        count_vowel +=1
    elif(string_input_list[i] in consonents):
        count_consonent+=1

print(f'No. of vowels: {count_vowel} \n No. of consonents: {count_consonent}')

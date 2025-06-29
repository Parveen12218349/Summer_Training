from myexceptions.prjexceptions import AgelimitError

per_name = input('Name :')
per_age = int(input('Age :'))

try:
    if per_age < 18:
        raise AgelimitError('Not eligible')
except AgelimitError as ale:
    print(ale)
else: print('Eligible !! ')
num = int(input('Enter The End: '))
sum = 0
for n in range(1,num+1,2):
    sum += n**2

print(f'Sum of Squares: {sum}')

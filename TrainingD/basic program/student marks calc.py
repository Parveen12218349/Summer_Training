
def calculate_total_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    avg = total/3
    return total, avg



sname = input('Enter name')
mark1 = int(input('Mark1: '))
mark2 = int(input('Mark2: '))
mark3 = int(input('Mark3: '))

Total, average = calculate_total_average(mark1, mark2, mark3)
print(f'Name :{sname} Total: {Total} Avg: {average}')
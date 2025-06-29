from oop.bikes import Bikes

brnd = input('Brand   ')
bknm = input('Bike Name   ')
rpd = int(input('Rent   '))


bkobj = Bikes(brand=brnd, rent=rpd, bkname=bknm)
days = int(input('NO of days '))
print(f'Bike {bkobj.bikename} for {days} is  {bkobj.calculate_rent(days)}')
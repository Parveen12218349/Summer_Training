num1=int(input())
num2=int(input())
nums= [1,2,3]
ans = 0
try:
    ans = num1//num2
    element = nums[5]
except ZeroDivisionError:
    print("Don't give zero in num2")

except IndexError:
    print('Watch the index')
except:
    print('oops something went wrong')
else:
    print(f'Quo : {ans}')
    print(f'Element : {element}')
finally:
    print('Done')
a = int (input('Enter the first number:'))
b = int (input('Enter the second number:'))

if (b==0):
    raise ZeroDivisionError('this program is not meant to divide number by zero')
else:
    print(f'the division of a/b is {a/b}')

print('you are here without crasing the program')
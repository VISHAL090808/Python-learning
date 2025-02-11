try:
    a = int (input('Enter the number :'))
    b = int (input('Enter the number :'))
    print (a/b)
except ZeroDivisionError as z:
    print('infinite (∞)')


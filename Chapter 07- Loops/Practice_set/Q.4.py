number = int (input('Enter the number :'))

for i in range (2, number):
    if number%i==0:
        print('this is not a prime number')
        break
else:
    print('this is a prime number')
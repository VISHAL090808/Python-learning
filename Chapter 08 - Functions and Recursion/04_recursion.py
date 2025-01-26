'''
factorial(0)= 1 
factorial(1)= 1
factorial(2)= 1 x 2
factorial(3)= 1 x 2 x 3
factorial(4)= 1 x 2 x 3 x 4
factorial(5)= 1 x 2 x 3 x 4 x 5


factorial(n) = n * (n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial (n-1)


n = int (input ('Enter the number :'))

print (f'the factorial of the given value is : { factorial(n)}')


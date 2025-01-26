n = int(input('Enter the number :'))
for i in range (1, n+1):
    print(' '* (n-i), end='')
    print('*'* (2*i-1))
    # print('')

    # print(' ' * (n-i) + '*'* (2*i-1) ) # can also write like this (concatenation)

def inch(n):
    cms= n*2.54 
    return cms

n= int(input('Enter the value in inches : '))

print(f'the centimeter value of {n} inch is: {inch(n)}')
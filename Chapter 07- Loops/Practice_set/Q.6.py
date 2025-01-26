number= int(input('Enter the number :'))

product = 1

for i in range (1, number+1):  
    product= product*i
    i += 1

print(f'the factorial of {number} is {product}')



def greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3 and n1>n3):
        return n2
    elif(n3>n2 and n3>n1 ):
        return n3

n1 =int(input('Enter the number :'))
n2 =int(input('Enter the number :'))
n3 =int(input('Enter the number :'))

print(f'above three {greatest(n1, n2 , n3)} is the greatest of all ') 
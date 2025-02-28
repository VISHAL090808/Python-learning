from functools import reduce
l= [10,25,6,45,88,52,40,80]

def greater (a, b):
    if (a>b):
        return a 
    return b 

print(reduce(greater, l))
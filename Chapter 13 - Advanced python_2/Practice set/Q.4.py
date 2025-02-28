def divisible5(n):
    if (n%5==0):
        return True
    return False

a= [10,25,6,45,88,52,40,80]
f= list(filter(divisible5, a))
print(f)
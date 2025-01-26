def f_to_c(f):
    c= 5*(f-32)/9
    return c
   
f = int(input('Enter the fahrenheit value :'))

print(f'Enter temperature in fahrenheit : {round(f_to_c(f),  2)}°C')
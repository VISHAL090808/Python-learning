try : 
    a = int(input('Enter the number :'))
    print(a)

except ValueError as v: #this will run (show) for value error
    print('hey')
    print(v)

except Exception as e: 
    print(e)

print( 'thank you')
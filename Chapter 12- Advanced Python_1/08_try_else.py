try : 
    a = int(input('Enter the number :'))
    print(a)

except Exception as e: 
    print(e)
else: # else only runs when the code will successfully passes through (try)
    print( 'thank you')
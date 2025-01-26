a = int(input('Enter the age:'))

#if statement no.1
if(a%2==0):                          #if can be used alon, else & elif can't
    print('the number is even')    
#End of if statement no. 1

#if statement no.2
if(a>=18):
    print('You are above the age of consent')
    print('your are allowed')

elif(a==0):

    print('you are entering invalid age***')    
    
elif(a<0):
    print('the age is not corrrect  ')    

else: 
    print('You are below the age of consent')

#End of if statement no. 2
    
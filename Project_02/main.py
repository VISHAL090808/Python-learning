import random 

n = random.randint(1, 50)
a = -1
guess = 0

while(a!=n):  
    a= int (input('Guess the number :'))

    if(a>n):
        print('Lower number please!')
        guess+=1
    elif (a<n):
        print('higher number please!')
        guess+=1

print(f'you have guessed the right number in {guess} attempts')
    








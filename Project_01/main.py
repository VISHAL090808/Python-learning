'''
-1 for snake
 0 for water
 1 for gun

'''
import random

computer = random.choice([-1, 0, 1])
youstr = input ('Enter your choice : ')

youdict = { 'snake': -1, 'water': 0, 'gun': 1}

you= youdict[youstr]
reversedict={-1: 'snake', 0 : 'water', 1: 'gun'}


#by now we have 2 numbers (variables), you and computer

print(f'you choose {reversedict[you]}\n computer choose {reversedict[computer]}')

if (computer == you):
    print('its a draw')
else:
    if(computer==-1 and you ==0):
        print('you lose')
    elif(computer==-1 and you==1):
        print('you won')
    if(computer==0 and you ==1):
        print('you lose')
    elif(computer==0 and you==-1):
        print('you won')
    if(computer==1 and you ==-1):
        print('you lose')
    elif(computer==1 and you==0):
        print('you won')
    else:
        'somthing went wrong'

p1= 'like this'
p2= 'won'
p3='Make a lot of money'
p4= 'Click this'

message = input('Enter the text :')


if p1 in message or p2 in message or p3 in message or p4 in message :
    print('this message is a spam')

else:
    print ('this is not a spam')
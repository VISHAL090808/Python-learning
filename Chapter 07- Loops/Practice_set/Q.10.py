number = int (input('Enter the number :'))

table = 0
for i in range (10, 0, -1) :
    table = (number*i)
    print(f'{number} X {i} =', table)

#below is another way to do this task
    
# for i in range (1, 11) :
#     print(f'{number} X {(11-i)} =', number*(11-i))
    

marks_1 = int(input('Enter the marks : '))
marks_2 = int(input('Enter the marks : '))
marks_3 = int(input('Enter the marks : '))

total_percentage=( 100*(marks_1 + marks_2 + marks_3))/300

if total_percentage>=40 : #and marks_1>=33 and marks_2>=33 and marks_3>=33 
    print('you are passed')
else:
    print('you failed in the exam ! try next year')
    
#below is the long way to get and answer

# sub1 = (100*marks_1)/100
# sub3 = (100*marks_3)/100
# sub2 = (100*marks_2)/100

# if sub1>33:
#     print('you are passed in sub1')

# if sub2>33:
#     print('you are passed in sub2')

# if sub3>33:
#     print('you are passed in sub3') 
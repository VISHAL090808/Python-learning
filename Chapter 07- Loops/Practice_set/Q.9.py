# n= int(input('Enter the number :'))

# for i in range (1, n+1):
#     if i==1 or i==n :
#         print('*'*n, end='')
#     else:
#         print('*', end='')
#         print(' '*(n-2), end='')
#         print('*', end='')
#     print('')

# practice

# n= int(input('Enter the number :'))

# for i in range (1, n+1):
#     if (i==1 or i==n):
#         print('*'*i, end='')
#     else:
#         print('*', end='')
#         print(' '*(i-2), end='')
#         print('*', end='')
#     print('')


 
# n = int(input("Enter the number: "))
# n= 5

# for i in range(1,n+1):
#     print(' ' * (n-i), end='')
#     for j in range(1,i+1):
#         if (i > 2 and (j!=1 and j!=i)):
#             print(' ' * 2, end='')
#             continue
#         print('*', end='')
#         print(' ', end='')
#     print('')

# for i in range(n-1,0,-1):
#     print(' ' * (n-i), end='')
#     for j in range(i,0,-1):
#         if (i > 2 and (j!=1 and j!=i)):
#             print(' ' * 2, end='')
#             continue
#         print('*', end='')
#         print(' ', end='')
#     print('')
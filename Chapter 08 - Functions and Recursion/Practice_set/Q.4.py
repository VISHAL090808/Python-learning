# def line(n):
#     for i in range (n, 0, -1):
#         if(i==n ):
#             print('*'*n)
#         else:
#             print('*'*(i))
            
# print( line(8))

def pattern (n):
    if(n==0):
        return
    print('*'*n)
    pattern (n-1)

pattern(4)
# def sum (n):
#     sum = 0
#     if(n==1):
#             return 1
#     for i in range (1, n+1):
            
#             sum+=i

#     return sum

# print(f'the sum of {sum(1)}')
#can we use for loop under the functions 

# harry ke code main jo sum ho raha ha uski value kaha save ho rahi hai time stamp -(5:25:43) 
def sum (n):
       if(n==1):
            return 1
                
       return n + sum(n-1)
print(f'the sum of 1 to n is : {sum(4)}')


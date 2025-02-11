list = [2,3,4,5,6]

squaredlist =[]

# for item in list :
#     squaredlist.append(item*item)

# we can simplify this proccess using list comprehension

squaredlist= [i*i for i in list]
print (squaredlist)
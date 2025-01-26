# f = open(r'd:\Python\Chapter 09 - file\file.txt ')
# print(f.read())
# f.close()

#above can be also achived like this

with open (r'd:\Python\Chapter 09 - file\file.txt ') as f :
    print(f.read())


# you don't have to explicitly close file 
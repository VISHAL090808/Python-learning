with open (r'd:\Python\Chapter 09 - file\Practice_set\file.txt_1','r') as f:
    content1=f.read()
    
with open (r'd:\Python\Chapter 09 - file\Practice_set\file.txt_2','r') as f:
    content2=f.read()

if (content1==content2):
    print('the content of both file is identical an present is both file simultaneously')
else:
    print('Oops! content is not matching')
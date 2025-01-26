with open (r'd:\Python\Chapter 09 - file\Practice_set\poem.txt') as f:
    
    c = f.read()
    if('how' in c):
        print('given word is found in the file')
    else:
        print('Oops!')
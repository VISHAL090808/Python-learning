words = ["donkey", 'cool', 'bad', 'dumb']

with open (r"d:\Python\Chapter 09 - file\file.txt", 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '#'*len(word))

with open (r"d:\Python\Chapter 09 - file\file.txt", 'w') as f:
    f.write(content)

    
        

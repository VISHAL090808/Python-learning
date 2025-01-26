def rem(l, word):
    n=[]
    for item in l:
        if (item != word):
            n.append(item.strip(word))
    return n

l=['vishal', 'jack', 'larry', 'jan', 'an']

print (rem(l, "an"))
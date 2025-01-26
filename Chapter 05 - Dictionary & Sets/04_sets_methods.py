a={4,5,5,6,55,"harry",} 

# a.add(365)
a.update([1,5,6]) #items do not repate in sets 
a.remove(5) # by this you can remove single element
# remove = {4,5} #below are the two ways to remove multiple elements
# a.difference_update(remove) #1
# a= a- remove #2
print(a, type(a))

new_a = a.copy()
print(new_a)
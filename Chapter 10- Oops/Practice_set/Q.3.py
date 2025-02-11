class check:
    a = 3


object =check()

print(object.a)#prints the class attribute bcz instance attribute is not present

object.a = 0 #instance attribute is set 
print(object.a)# prints the instance attribute bcz instance

print(check.a)# prints the class attribute

#conslusion = class attribute is not changed
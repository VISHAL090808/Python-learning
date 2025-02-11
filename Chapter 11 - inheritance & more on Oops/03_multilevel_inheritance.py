class Employee:
    a=1

class programer(Employee):
    b=2

class manager(programer):
    c=3


o=Employee()
print(o.a) #prints the a attribute
# print(o.b) #showa error as there is no b attribute in employee class

o=programer()
print(o.a, o.b)


o=manager()
print(o.a, o.b, o.c)

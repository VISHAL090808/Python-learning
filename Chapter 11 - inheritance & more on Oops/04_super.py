class Employee:
    def __init__(self):
        print('constructer of Employeee')
    a=1

class programer(Employee):
    def __init__(self):
    
        print('constructer of programer')
    b=2

class manager(programer):
    def __init__(self):
        super().__init__()
        print('constructer of manager')
    c=3


# o=Employee()
# print(o.a) #prints the a attribute
# # print(o.b) #showa error as there is no b attribute in employee class

# o=programer()
# print(o.a, o.b)

o=manager()
print(o.a, o.b, o.c)

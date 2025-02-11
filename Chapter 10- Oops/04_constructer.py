class Employee :
    language = 'py' #This is class attribute
    salary = 1200000
    def __init__(self, name, languae, salary):

        # here self.name refers as variabble(as it written left side of def init) and = name is value like (vishal, harry etc.)
        self.name =name
        self.language =languae
        self.salary= salary
        

    def getinfo(self):
        print(f'the language is { self.language}, and the salary is {self.salary}')

    @staticmethod
    def greet ():
        print ('good morning')


harry =Employee( 'vishal', 'javascript', 12000)
print(harry.name, harry.language, harry.salary)

harry.getinfo()


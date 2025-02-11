class Employee :
    language = 'py' #This is class attribute
    salary = 1200000

    @staticmethod
    def greet ():
        print ('good morning')

    def getinfo(self):
        print(f'the language is { self.language}, and the salary is {self.salary}')


harry = Employee ()
harry.language= 'java' 

# harry.getinfo()
harry.greet() # why can't we call function like this- getinfo()
harry.getinfo()


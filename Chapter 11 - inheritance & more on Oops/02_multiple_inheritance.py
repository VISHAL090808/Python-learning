class Employee :
    company = 'ITC'
    name = 'vishal'
    salary= 12000
        
    def show (self):
        print(f'the name of employee is {self.name} and salary of him is {self.salary}')

class coder:
    language= 'Python'
    def printlanguages(self):
        print(f'out of all languages here is your language {self.language}')

# class programer :
#     company = 'ITC Infotech'
#     def show (self):
#         print(f'the name of employee is {self.name} and salary of him is {self.salary}')

#     def showlanguage(self):
#         print(f'the name is {self.name} and he is good in {self.language}')

class programer(Employee, coder):
    company = 'ITC Infotech'
    def showlanguage(self):
        print(f'Name of employee is {self.name} and he is good in {self.language}')

a= Employee()
b= programer()
    
print(a.company, b.company)
b.show()
b.showlanguage()
b.printlanguages()

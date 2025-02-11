class Employee :
    company = 'ITC'
    name = 'vishal'
    salary= 12000
        
    def show (self):
        print(f'the name of employee is {self.name} and salary of him is {self.salary}')

# class programer :
#     company = 'ITC Infotech'
#     def show (self):
#         print(f'the name of employee is {self.name} and salary of him is {self.salary}')

#     def showlanguage(self):
#         print(f'the name is {self.name} and he is good in {self.language}')

class programer(Employee):
    company = 'ITC Infotech'
    def showlanguage(self):
        print(f'Name of employee is {self.name} and he is good in {self.language}')

a= Employee()
b= programer()
    
print(a.company, b.company)


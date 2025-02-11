class Employee:
    a=1
    @classmethod #through class method you can access class attribute
    def show(cls):
        print(f'the value of class attribute is {cls.a}')

    @property
    def name (self):
        return f'{self.fname} {self.lname}'
    
    @name.setter
    def name (self, value):
        self.fname= value.split(' ') [0]
        self.lname= value.split(' ') [1]

e=Employee()
e.a=45

e.name ='jack sparrow'
print(e.name)

e.show()
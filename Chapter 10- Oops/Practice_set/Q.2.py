class calculator :
    def __init__(self, n):
        self.n = n 

    def square(self):
        print(f'the square of given number is {self.n*self.n}')

    def cube(self):
        print(f'the cube of given number is {self.n*self.n*self.n}')

    def square_root(self):
        print(f'the square_root of given number is {self.n**1/2}')

a= calculator(5)
a.square()
a.cube()
a.square_root()

          

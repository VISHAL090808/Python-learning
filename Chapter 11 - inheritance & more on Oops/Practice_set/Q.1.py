class Twovector():
    def __init__(self, i, j):
        self.i= i
        self.j= j 
    def show(self):
        print(f'the value is {self.i}i and {self.j}j')

class Threevector(Twovector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k 
     
    def show(self):
        print(f'the value is {self.i}i and {self.j}j and {self.k}k')


a = Twovector(6, 5)
a.show()

b = Threevector(4, 3, 2)
b.show()
        
        

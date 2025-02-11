class complex :
    def __init__(self, r, i):
        self.r = r
        self.i = i 

    def __add__(self, c2):
        return complex (self.r + c2.r, self.i + c2.i) # here we calling the complex class into the class itself and the class is autometically 
     # creating an object ( i and r) and assigning values into them, that's why we are using STR method to print those objects                                            

        # return f"{self.r + c2.r} + {self.i + c2.i}i" in this way you don't have to use STR method to print (C1 + C2)

    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)

    def __str__(self):
        return f" {self.r} + {self.i}i"
        

c1 = complex (1, 2)
c2 = complex (3, 4)
print (c1)
print (c2)
print (c1 + c2)
print (c1 * c2)


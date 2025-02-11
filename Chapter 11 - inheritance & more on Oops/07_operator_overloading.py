class number :
    def __init__(self, n):
        self.n= n

    def __add__(obj1, obj2 ):
        return obj1.n + obj2.n 


n = number(1)
m = number(2)

print(n + m)

        
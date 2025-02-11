from random import randint
class train:
    def __init__(self, trainNO):
        self.trainNo= trainNO

    def book(self, frm, to):
        print(f'your ticket from {frm} to {to} in train {self.trainNo} is booked successfully ')
    def getstatus(self):
        print(f'train no {self.trainNo} is running on time')

    def getfare(self, frm, to):
        print(f'Total ticket fare of  your journey from {frm} to {to} in train no {self.trainNo} is RS. {randint(222, 2000)} ')
        
    
t= train(14115)

t.book('chhatarpur', 'indore')
t.getstatus()

t.getfare('chhatarpur', 'indore')
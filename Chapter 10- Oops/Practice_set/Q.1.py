class programers:
    company = 'Microsoft'
    def __init__(self, name, salary, shift ):
        self.name= name
        self.salary= salary
        self.shift = shift


harry= programers( 'vishal', 12000, 'night' )
print(harry.name, harry.salary, harry.shift, harry.company )

rohan= programers( 'rohan', 36000, 'day' )
print(rohan.name, rohan.salary, rohan.shift, rohan.company )
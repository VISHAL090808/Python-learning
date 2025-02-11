a = 1  # Global variable

def fun():
    global a  # Declaring 'a' as global to modify its value
    a = 3  # Updating the global variable 'a'
    print(a)  # Prints the updated global value (3)

fun()
print(a)  # Prints 3 because 'a' was modified globally inside the function

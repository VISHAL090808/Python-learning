
n =int (input('enter the number :'))

table = [n*i for i in range (1,11)]

with open (r"D:\Python\Chapter 12- Advanced Python_1\Practice_set\table.txt", 'a') as f:
    f.write(f'tabel of {n}: {table}\n')



# def generate(n):
#     import os 
#     folder_path= r"d:\Python\Chapter 09 - file\Practice_set\tables"
#     os.makedirs(folder_path, exist_ok= True)

#     table = ''
#     for i in range (1, 11):
#         file_path= os.path.join(folder_path, f"table_{n}.txt")
#         table= print(f"{n} X {i} = {n*i}")
       
#         with open(file_path, 'w')as f:

#             f.write(table)


# for i in range (2, 21):
#     generate(i)

#above code is not correct

def generate(n):
    import os  
    folder_path = r"d:\Python\Chapter 09 - file\Practice_set\tables"
    os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists

    file_path = os.path.join(folder_path, f"table_{n}.txt")  # File path

    table = ""  # Initialize an empty string to store the table

    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"  # Append table content to the string

    # Write the table content to the file
    with open(file_path, "w") as f:
        f.write(table)

    print(f"Table of {n} saved in {file_path}")

# Generate tables from 2 to 20
for i in range(2, 21):
    generate(i)



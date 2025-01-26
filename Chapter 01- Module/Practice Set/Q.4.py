import os

# select the directory whose content you want to list
directory_path = '/'

# Use the os module to list the content
entries = os.listdir(directory_path)
       
# write a code to print the content of directory
for entry in entries:
    print(entry)

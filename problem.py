import os

#specify the directory You wat to list
directory_path = os.path.dirname('/New folder')

# list all file and directories in the specified path
contents = os.listdir(directory_path)

#print the contents of the directory
for item in contents:
    print(item)
    
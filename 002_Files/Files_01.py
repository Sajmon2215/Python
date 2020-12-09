import os

# /dir does not work since I am working on Windows
directory = "C:\\Program Files"
fileList = os.listdir(directory)
print('Number of files in ' + directory + ' is ' + str(len(fileList)))

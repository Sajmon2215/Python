import glob
path = '.\\TEST'

for fileName in glob.iglob(path + "**/**", recursive=True):
    print(fileName)
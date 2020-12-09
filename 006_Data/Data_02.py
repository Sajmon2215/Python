import csv
import re

rows = []
with open("test.csv", "r", newline="") as f:
    reader = csv.reader(f)
    print("*****Currently saved data*****")
    for i, row in enumerate(reader):
        rows.append(row)
        if i > 0:
            print(i, end=" ")
        for index, element in enumerate(row):
            if index < (len(row) - 1):
                print(element, end="    ")
            else:
                print(element)

print("What would you like to do?")
newRows = []
newRowsUsed = False
while True:
    print("1.Delete a record   2.Add a new record   3.Quit")
    choice = int(input())
    if choice == 1:
        isWrong = True
        while isWrong:
            print("Which element would you like to delete? Enter ID")
            deleteId = int(input())
            if 0 < deleteId < len(rows):
                for i, element in enumerate(rows):
                    if i != deleteId:
                        newRows.append(element)
                isWrong = False
                newRowsUsed = True
            else:
                print("Wrong input! please Try again!")
    elif choice == 2:
        if not newRowsUsed:
            newRows = rows
        isWrong = True
        while isWrong:
            print("Please enter in format\"Type,Manufacturer,Model\"")
            rowIn = input()
            if re.match(r'.*,.*,.*', rowIn):
                newRows.append(rowIn.split(","))
                print("Entry added!")
                isWrong = False
            else:
                print("Wrong entry!")
    elif choice == 3:
        if not newRowsUsed:
            newRows = rows
        isWrong = True
        with open("test.csv", "w+", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(newRows)
        exit()

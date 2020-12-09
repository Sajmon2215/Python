toReplace = {"i" : "oraz", "oraz" : "i", "nigdy" : "prawie nigdy",
             "dlaczego" : "czemu", "Dlaczego" : "Czemu", "Nigdy" : "Prawie nigdy"}
fileName = ''
with open(fileName, 'r', encoding='UTF8') as f:
    text = f.read()

textLines = text.splitlines()

tempLines = []
for line in textLines:
    tempList = []
    for word in line.split():
        if word in toReplace:
            tempList.append(toReplace[word])
            continue
        tempList.append(word)
    tempLines.append(tempList)

resultLine = ""
for element in tempLines:
    tempLine = " "
    tempLine = tempLine.join(element)
    resultLine += tempLine + '\n'
print(resultLine)
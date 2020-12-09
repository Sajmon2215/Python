toDelete = ["się", "i", "oraz", "nigdy", "dlaczego", "Dlaczego", "Nigdy"]
specialSigns = [".", ",", "?", "!"]
with open('test.txt', 'r', encoding='UTF8') as f:
    text = f.read()

for word in toDelete:
    text = text.replace(" {} ".format(word), " ")
    text = text.replace("{} ".format(word), "")
    for sign in specialSigns:
        text = text.replace(" {}{}".format(word, sign), sign)
        text = text.replace("{}{} ".format(word, sign), sign)

print(text)
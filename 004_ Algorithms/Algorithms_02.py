import random


def bubble_sort(in_list):
    for i in range(len(in_list)):
        for j in range(len(in_list) - 1):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list


randomNumbers = []
for x in range(50):
    randomNumbers.append(random.randint(0, 100))

sortedNumbers = randomNumbers.copy()
sortedNumbers = bubble_sort(sortedNumbers)
sortedBuiltin = randomNumbers.copy()
sortedBuiltin.sort()
print(randomNumbers)
print(sortedNumbers)
print(sortedBuiltin)
if sortedNumbers == sortedBuiltin:
    print("Lists are the same!")
else:
    print("Lists are not the same")

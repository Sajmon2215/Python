import random


def matrix_sum(matrix1, matrix2):
    if len(matrix1) == len(matrix2):
        result = []
        for i in range(len(matrix1)):
            temp_result = []
            for j in range(len(matrix1)):
                temp_result.append(matrix1[i][j] + matrix2[i][j])
            result.append(temp_result)
        return result
    else:
        print("Wrong matrix size!")


m_size = 128
m1 = []
m2 = []
for x in range(m_size):
    tempList1 = []
    tempList2 = []
    for y in range(m_size):
        tempList1.append(random.randint(0, 100))
        tempList2.append(random.randint(0, 100))
    m1.append(tempList1)
    m2.append(tempList2)

mSum = matrix_sum(m1, m2)

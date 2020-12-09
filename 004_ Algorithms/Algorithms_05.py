import random

m_size = 8
m1 = []
m2 = []
for x in range(m_size):
    tempList1 = []
    tempList2 = []
    for y in range(m_size):
        tempList1.append(random.randint(0, 5))
        tempList2.append(random.randint(0, 5))
    m1.append(tempList1)
    m2.append(tempList2)
result = []
for i in range(len(m1)):
    tempList = []
    for j in range(len(m1)):
        s = 0
        for k in range(len(m1)):
            s += m1[i][k] * m2[k][j]
        tempList.append(s)
    result.append(tempList)

for row in result:
    print(row)

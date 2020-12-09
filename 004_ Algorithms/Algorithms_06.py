import random
import numpy


def det(m):
    retval = 0
    index = list(range(len(m)))

    if len(m) == 2 and len(m[0]) == 2:
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]

    for i in index:
        m_copy = m.copy()
        m_copy = m_copy[1:]

        for j in range(len(m_copy)):
            m_copy[j] = m_copy[j][0:i] + m_copy[j][i+1:]

        sign = (-1) ** (i % 2)
        s_det = det(m_copy)
        retval += sign * m[0][i] * s_det

    return retval


m_size = 8
m1 = []
for x in range(m_size):
    tempList1 = []
    for y in range(m_size):
        tempList1.append(random.randint(0, 5))
    m1.append(tempList1)

for row in m1:
    print(row)

print("Calculated determinant: {}".format(det(m1)))
print("Numpy determinant: {}".format(numpy.linalg.det(numpy.array(m1))))

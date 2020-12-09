def scalar(vector1, vector2):
    result = 0
    if len(vector1) == len(vector2):
        for i in range(len(vector1)):
            result += vector1[i] * vector2[i]
    elif len(vector1) > len(vector2):
        diff = len(vector1) - len(vector2)
        for i in range(diff):
            vector2.insert(0, 0)
        for i in range(len(vector1)):
            result += vector1[i] * vector2[i]
    elif len(vector1) < len(vector2):
        diff = len(vector2) - len(vector1)
        for i in range(diff):
            vector1.insert(0, 0)
        for i in range(len(vector1)):
            result += vector1[i] * vector2[i]
    return result


v1 = [1, 2, 12, 4]
v2 = [2, 4, 2, 8]
print("The result is: {}".format(scalar(v1, v2)))

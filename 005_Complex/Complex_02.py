from Complex_01 import Complex
import re


def number_split(s):
    complex_search = re.compile(r'(?<=\()\d\s*[+-]\s*\d(?=i*\))')
    numbers = re.findall(complex_search, s)
    n1 = re.findall(r'[+-]*\s*\d', str(numbers[0]))
    n2 = re.findall(r'[+-]*\s*\d', str(numbers[1]))
    res1 = []
    res2 = []
    for element in n1:
        if "+" in element:
            res1.append(re.search(r'\d', element).group(0))
        elif "-" in element:
            res1.append("-" + re.search(r'\d', element).group(0))
        else:
            res1.append(element)
    for element in n2:
        if "+" in element:
            res2.append(re.search(r'\d', element).group(0))
        elif "-" in element:
            res2.append("-" + re.search(r'\d', element).group(0))
        else:
            res2.append(element)

    return Complex(float(res1[0]), float(res1[1])), Complex(float(res2[0]), float(res2[1]))


print("Please enter your Complex number equation, using format (2 + 4i) + (2 - 1i), available operations: + - * /")
stringIn = input()

if re.match(r'\(\d\s*[+-]\s*\di*\)\s*\+\s*\(\d\s*[+-]\s*\di*\)', stringIn):
    c1, c2 = number_split(stringIn)
    print(str(c1 + c2))
elif re.match(r'\(\d\s*[+-]\s*\di*\)\s*\-\s*\(\d\s*[+-]\s*\di*\)', stringIn):
    c1, c2 = number_split(stringIn)
    print(str(c1 - c2))
elif re.match(r'\(\d\s*[+-]\s*\di*\)\s*\*\s*\(\d\s*[+-]\s*\di*\)', stringIn):
    c1, c2 = number_split(stringIn)
    print(str(c1 * c2))
elif re.match(r'\(\d\s*[+-]\s*\di*\)\s*/\s*\(\d\s*[+-]\s*\di*\)', stringIn):
    c1, c2 = number_split(stringIn)
    print(str(c1/c2))
else:
    print("Wrong input line!")
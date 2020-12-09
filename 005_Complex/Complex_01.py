import math


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im,
                       self.im * other.re + self.re * other.im)

    def __truediv__(self, other):
        denominator = float(other.re**2 + other.im**2)
        return Complex((self.re * other.re + self.im * other.im) / denominator,
                       (self.im * other.re - self.re * other.im) / denominator)

    def __abs__(self):
        return math.sqrt(self.re**2 + self.im**2)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{} {}i".format(self.re, self.im)

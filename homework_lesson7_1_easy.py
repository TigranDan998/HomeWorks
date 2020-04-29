#задача1_easy

import math

class Side:
    def width(self,A,B):
        return round(math.sqrt(sum(tuple(map(lambda a,b:(b-a)**2,A,B)))),2)

class Triangle(Side):
    def __init__(self,A,B,C):
        self._A=A
        self._B=B
        self._C=C
    def sides(self):
        return {'AB': self.width(self._A, self._B),
                'BC': self.width(self._B, self._C),
                'CA': self.width(self._C, self._A)
                }
    def perimeter(self):
        return round(self.sides()['AB'] +
                     self.sides()['BC'] +
                     self.sides()['CA'], 2)
    def area(self):
        return round((lambda p, a, b, c:
                      math.sqrt(p * (p - a) * (p - b) * (p - c)))
                      (self.perimeter() / 2,
                       self.sides()['AB'],
                       self.sides()['BC'],
                       self.sides()['CA']), 2)

A1,A2,A3=(3,4),(1,2),(5,3)

triangle=Triangle(A1,A2,A3)
print ('Треугольник:\n Площадь: {triangle.area()} кв.см.\n Периметр: {triangle.perimeter()} см')

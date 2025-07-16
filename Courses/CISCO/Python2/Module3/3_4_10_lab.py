'''
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Expected ouptut:
3.414213562373095

'''

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
       self.__x = x
       self.__y = y
       
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def distance_from_xy(self, x, y) ->float:
        delta_x = abs(self.__x - x)
        delta_y = abs(self.__y - y)
        return math.hypot(delta_x, delta_y)
        

    def distance_from_point(self, point) -> float:
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1: Point, vertice2: Point, vertice3: Point):
        self.__point1=vertice1
        self.__point2 = vertice2
        self.__point3 = vertice3
        
        

    def perimeter(self):
        a = self.__point1.distance_from_point(self.__point2)
        b = self.__point2.distance_from_point(self.__point3)
        c = self.__point1.distance_from_point(self.__point3)
        return a + b + c

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())
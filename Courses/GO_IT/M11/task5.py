'''
Implement the __str__ magic method for the Point and Vector classes. For the Point class, the method must return a string of the form Point(x,y), and for the Vector class - the string Vector(x,y), as in the example below (instead of x/y, you must substitute the coordinates of the class instance):

point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)
'''
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
    
    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
                self.coordinates.x = value
        elif index == 1:
                self.coordinates.y = value
        else:
                raise ValueError("Index should be in [0,1]")            

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise ValueError("Index should be in [0,1]")
        
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
if __name__ == "__main__":
    point = Point(1, 10)
    vector = Vector(point)

    print(point)  # Point(1,10)
    print(vector)  # Vector(1,10)
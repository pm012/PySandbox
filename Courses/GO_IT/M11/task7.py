'''
Implement the operations of adding and subtracting vectors for the Vector class. That is, redefine the mathematical operators __add__ and __sub__ for it

There are two vectors: a with coordinates (x1, y1) and b with coordinates (x2, y2).

Then the addition of vectors b + a creates a new vector with coordinates (x2 + x1, y2 + y1). Subtraction is the opposite operation, b - a becomes a new vector with coordinates (x2 - x1, y2 - y1).

Example:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)
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
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        point = Point(self.coordinates.x + vector.coordinates.x, self.coordinates.y + vector.coordinates.y)
        return Vector(point)

    def __sub__(self, vector):
        point = Point(self.coordinates.x - vector.coordinates.x, self.coordinates.y - vector.coordinates.y)
        return Vector(point) 

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"    
if __name__ == "__main__":
    vector1 = Vector(Point(1, 10))
    vector2 = Vector(Point(10, 10))

    vector3 = vector2 + vector1
    vector4 = vector2 - vector1

    print(vector3)  # Vector(11,20)
    print(vector4)  # Vector(9,0)
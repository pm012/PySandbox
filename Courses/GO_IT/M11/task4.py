'''
Implement the Vector class. The coordinates property defines the 
coordinates of the vector and is an instance of the Point class. 
As you know, a vector is a directed segment with a beginning and an end. 
The beginning will be at the point (0, 0), 
and the end of the vector will be set by the coordinates attribute.

Implement the ability to access the coordinates of an instance of the Vector 
class through square brackets:

vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Set the x coordinate of the vector to 10

print(vector[0])  # 10
print(vector[1])  # 10

To get a value using the square brackets of the print(vector[0]) object, 
you have to implement the __getitem__ method of the Vector class.

To store the value of a vector's coordinates using an index, like vector[0] = 10,
 implement the method __setitem__ in the Vector class.

The x coordinate is accessed at index 0, and the y coordinate is 
accessed at index 1.


task 5: implement the __str__ method for the Point class and the Vector class.

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
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        
        if index ==0:
            self.coordinates.x = value 
        elif index == 1:
            self.coordinates.y = value 
        else:
            raise IndexError("Index out of range")
        

    def __getitem__(self, index):
        #return self.coordinates.x if index == 0 else self.coordinates.y
        if index ==0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Index out of range")
        
    def __str__(self):
        return f"Vector({self.coordinates.x}, {self.coordinates.y})"
        
if __name__ == "__main__":
    point = Point(1, 10)
    vector = Vector(point)

    print(vector.coordinates.x)  # 1
    print(vector.coordinates.y)  # 10

    vector[0] = 13  # Set the x coordinate of the vector to 13

    print(vector[0])  # 13
    print(vector[1])  # 10
    print(vector)  # Vector(13, 10)
    print(point)  # Point(13, 10)
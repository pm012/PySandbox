'''
In the Point class, two attributes are declared through the __init__ constructor: x and y coordinates. You can hide access to them with a double underscore: __x and __y.

Implement the setter and getter mechanisms for the Point class for the __x and __y attributes using the property and setter decorators.

Example:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y):
        self.__y = new_y

if __name__ == "__main__":
    point = Point(5, 10)

    print(point.x)
    print(point.y)
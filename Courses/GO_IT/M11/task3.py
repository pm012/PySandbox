'''
In the Point class, add a check for the entered value to the setter mechanism
 of the x and y properties. Allow the x and y properties to be set 
 for an instance of the class only if they have a numeric value (int or float).

Example:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10
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
        if isinstance(x, (int, float)):
            self.__x=x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y=y

if __name__ == "__main__":
    point = Point("a", 10)

    print(point.x)  # None
    print(point.y)  # 10
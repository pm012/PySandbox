'''
Create a class Point, which will be responsible for displaying a geometric point on the plane.

Implement the initialization of two attributes through the __init__ constructor: the x and y coordinates.

Example:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

if __name__ == "__main__":
    point = Point(5,10)
    print(point.x)
    print(point.y)
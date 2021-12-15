class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

#print(a)
#print(b)

#################
# class Point:
#     pass
#
#
# p1 = Point()
# p2 = Point()
#
# p1.x = 5
# p1.y = 4
#
# p2.x = 3
# p2.y = 6
#
# print(p1.x, p1.y)
# print(p2.x, p2.y)
#################
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
#
#
# p = Point()
# p.reset()
# print(p.x, p.y)
#################
import math
class Point:
    def __init__(self, x, y):
        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin."""
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def reset(self):
        "Reset the point back to the geometric origin: 0, 0"
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        )

# how to use it:
# point1 = Point()
# point2 = Point()
# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))
# assert point2.calculate_distance(point1) == point1.calculate_distance(point2 )
# point1.move(3, 4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))

# Constructing a Point
point = Point(3, 5)
print(point.x, point.y)
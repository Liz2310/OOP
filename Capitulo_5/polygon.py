"""To calculate the distance around the perimeter of the polygon, we
need to sum the distances between each point."""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Polygon:
    def __init__(self, points=None):
        """Accepts a list of Point objects. In fact, let's allow it to
        accept tuples too, and we can construct the Point objects ourselves, if needed.

        Goes through the list and ensures that any tuples are converted to points.
        If the object is not a tuple, we leave it as is, assuming that it is either
        a Point object already, or an unknown duck-typed object that can act like a Point object."""

        points = points if points else [] #que hace esto?
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]] #self.vertices[0] adds the first point in order to calculate all around (cycle through all points, starting and ending in the first point)
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i + 1]) #calculates distance between every two points
        return perimeter


square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
print(square.perimeter())

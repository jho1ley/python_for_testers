from math import sqrt

class Point:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
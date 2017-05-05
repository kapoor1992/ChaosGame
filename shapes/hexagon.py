from math import sqrt
from shape import Shape

class Hexagon(Shape):
    total_vertices = 6
    
    def vertices(self):
        distance = 300
        top_y = sqrt(pow(distance, 2) - pow(150, 2))
        bot_y = -top_y

        self.vertex0 = [-150, -150]
        self.vertex1 = [-150, 150]
        self.vertex2 = [0, top_y]
        self.vertex3 = [150, 150]
        self.vertex4 = [150, -150]
        self.vertex5 = [0, bot_y]

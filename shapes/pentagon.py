from math import sqrt
from shape import Shape

class Pentagon(Shape):
    total_vertices = 5
    
    def vertices(self):
        distance = sqrt(2 * pow(200, 2))
        bot_right_x = distance / 2
        bot_left_x = -bot_right_x
        bot_y = -sqrt(pow(distance, 2) - pow(200 - bot_right_x, 2))

        self.vertex0 = [-200, 0]
        self.vertex1 = [0, 200]
        self.vertex2 = [200, 0]
        self.vertex3 = [bot_right_x, bot_y]
        self.vertex4 = [bot_left_x, bot_y]

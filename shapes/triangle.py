from math import sqrt
from shape import Shape

class Triangle(Shape):
    total_vertices = 3
    
    def vertices(self):
        x_low = -200
        y_low = -200
        x_mid = 0
        x_high = x_low * -1
        y_high = y_low + sqrt(pow(abs(x_low * 2), 2) - pow(x_mid - x_high, 2))

        self.vertex0 = [x_low, y_low]
        self.vertex1 = [x_mid, y_high]
        self.vertex2 = [x_high, y_low]    

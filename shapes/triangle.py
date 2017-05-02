from math import sqrt
from random import randint
from turtle import *
from shape import Shape
from util import lines

class Triangle(Shape):
    def vertices(self):
        x_low = -200
        y_low = -200
        x_mid = 0
        x_high = x_low * -1
        y_high = y_low + sqrt(pow(abs(x_low * 2), 2) - pow(x_mid - x_high, 2))

        self.vertex0 = [x_low, y_low]
        self.vertex1 = [x_mid, y_high]
        self.vertex2 = [x_high, y_low]    

    def outline(self):
        super(Triangle, self).outline()
        
        goto(self.vertex1)
        goto(self.vertex2)
        goto(self.vertex0)


    def plot(self):
        super(Triangle, self).plot()
        current = self.vertex0
        block = current

        for i in range(self.points):
            direction = randint(0, 2)

            if self.unique_next:
                while (block == direction):
                    direction = randint(0, 2)
                block = direction

            for j in range(self.halves):
                if direction == 0:
                    current = lines.midpoint(current, self.vertex0)
                if direction == 1:
                    current = lines.midpoint(current, self.vertex1)
                if direction == 2:
                    current = lines.midpoint(current, self.vertex2)

            penup()
            goto(current)
            dot(self.dot_size)
    
            if i % self.refresh_rate == 0:
                update()

        update()

from math import sqrt
from random import randint
from turtle import *
from shape import Shape
from util import lines

class Hexagon(Shape):
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

    def outline(self):
        super(Hexagon, self).outline()
        
        goto(self.vertex1)
        goto(self.vertex2)
        goto(self.vertex3)
        goto(self.vertex4)
        goto(self.vertex5)
        goto(self.vertex0)


    def plot(self):
        super(Hexagon, self).plot()
        current = self.vertex0
        block = current

        for i in range(self.points):
            direction = randint(0, 5)

            if self.unique_next:
                while (block == direction):
                    direction = randint(0, 5)
                block = direction

            for j in range(self.halves):
                if direction == 0:
                    current = lines.midpoint(current, self.vertex0)
                if direction == 1:
                    current = lines.midpoint(current, self.vertex1)
                if direction == 2:
                    current = lines.midpoint(current, self.vertex2)
                if direction == 3:
                    current = lines.midpoint(current, self.vertex3)
                if direction == 4:
                    current = lines.midpoint(current, self.vertex4)
                if direction == 5:
                    current = lines.midpoint(current, self.vertex5)

            penup()
            goto(current)
            dot(self.dot_size)
    
            if i % self.refresh_rate == 0:
                update()

        update()

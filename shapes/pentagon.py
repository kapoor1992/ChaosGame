from math import sqrt
from random import randint
from turtle import *
from shape import Shape
from util import lines

class Pentagon(Shape):
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

    def outline(self):
        super(Pentagon, self).outline()
        
        goto(self.vertex1)
        goto(self.vertex2)
        goto(self.vertex3)
        goto(self.vertex4)
        goto(self.vertex0)


    def plot(self):
        super(Pentagon, self).plot()
        current = self.vertex0
        block = current

        for i in range(self.points):
            direction = randint(0, 4)

            if self.unique_next:
                while (block == direction):
                    direction = randint(0, 4)
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

            penup()
            goto(current)
            dot(self.dot_size)
    
            if i % self.refresh_rate == 0:
                update()

        update()

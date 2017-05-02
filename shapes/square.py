from random import randint
from turtle import *
from shape import Shape
from util import lines

class Square(Shape):
    def vertices(self):
        self.vertex0 = [-200, -200]
        self.vertex1 = [-200, 200]
        self.vertex2 = [200, 200]
        self.vertex3 = [200, -200]

    def outline(self):
        super(Square, self).outline()
        
        goto(self.vertex1)
        goto(self.vertex2)
        goto(self.vertex3)
        goto(self.vertex0)


    def plot(self):
        super(Square, self).plot()
        current = self.vertex0
        block = current

        for i in range(self.points):
            direction = randint(0, 3)

            if self.unique_next:
                while (block == direction):
                    direction = randint(0, 3)
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

            penup()
            goto(current)
            dot(self.dot_size)

            if i % self.refresh_rate == 0:
                update()

        update()


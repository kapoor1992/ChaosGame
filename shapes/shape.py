from turtle import *
from random import randint
from util import lines

# handles up to and including a 10-vertex outline
class Shape(object):
    dot_size = 1
    outline_color = 'black'
    plot_color = 'red'

    def __init__(self, points, refresh_rate, halves, unique_next):
        self.points = points
        self.refresh_rate = refresh_rate
        self.halves = halves
        self.unique_next = unique_next

        speed(0)
        
        self.vertices()

    def vertices(self):
        pass

    def draw(self):
        self.outline()
        self.plot()

        done()

    def outline(self):
        color(self.outline_color)

        if self.total_vertices > 0:
            penup()
            goto(self.vertex0)
            pendown()
        if self.total_vertices > 1:
            goto(self.vertex1)
        if self.total_vertices > 2:
            goto(self.vertex2)
        if self.total_vertices > 3:
            goto(self.vertex3)
        if self.total_vertices > 4:
            goto(self.vertex4)
        if self.total_vertices > 5:
            goto(self.vertex5)
        if self.total_vertices > 6:
            goto(self.vertex6)
        if self.total_vertices > 7:
            goto(self.vertex7)
        if self.total_vertices > 8:
            goto(self.vertex8)
        if self.total_vertices > 9:
            goto(self.vertex9)

        goto(self.vertex0)

    def plot(self):
        color(self.plot_color)
        tracer(0, 0)

        current = self.vertex0
        block = current

        for i in range(self.points):
            direction = randint(0, self.total_vertices - 1)

            if self.unique_next:
                while (block == direction):
                    direction = randint(0, self.total_vertices - 1)
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
                if direction == 6:
                    current = lines.midpoint(current, self.vertex6)
                if direction == 7:
                    current = lines.midpoint(current, self.vertex7)
                if direction == 8:
                    current = lines.midpoint(current, self.vertex8)
                if direction == 9:
                    current = lines.midpoint(current, self.vertex9)

            penup()
            goto(current)
            dot(self.dot_size)
    
            if i % self.refresh_rate == 0:
                update()

        update()

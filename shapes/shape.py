from turtle import *

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

        penup()
        goto(self.vertex0)
        pendown()

    def plot(self):
        color(self.plot_color)
        tracer(0, 0)

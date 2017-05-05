from shape import Shape

class Square(Shape):
    total_vertices = 4
    
    def vertices(self):
        self.vertex0 = [-200, -200]
        self.vertex1 = [-200, 200]
        self.vertex2 = [200, 200]
        self.vertex3 = [200, -200]

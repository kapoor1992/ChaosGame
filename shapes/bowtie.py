from shape import Shape

class Bowtie(Shape):
    total_vertices = 8
    
    def vertices(self):
        self.vertex0 = [-200, -200]
        self.vertex1 = [-50, -50]
        self.vertex2 = [50, -50]
        self.vertex3 = [200, -200]
        self.vertex4 = [200, 200]
        self.vertex5 = [50, 50]
        self.vertex6 = [-50, 50]
        self.vertex7 = [-200, 200]

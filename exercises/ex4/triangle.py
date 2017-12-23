from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, vertices, base_length, height):
        super(Triangle, self).__init__(vertices)
        self.base_length = base_length
        self.height = height

    def get_area(self):
        return 0.5 * self.base_length * self.height

if __name__ == '__main__':
    t = Triangle(vertices=[(0,0), (2,0), (1, 3)], base_length=2, height=3)
    print t.get_perimeter()
    print t.get_area()
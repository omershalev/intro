from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, vertices, base_length, height):
        # TODO: add your code here
        pass

    def get_area(self):
        # TODO: add your code here
        pass

if __name__ == '__main__':
    t = Triangle(vertices=[(0,0), (2,0), (1, 3)], base_length=2, height=3)
    print t.get_perimeter() # expected: 8.32455532034
    print t.get_area() # expected: 3.0
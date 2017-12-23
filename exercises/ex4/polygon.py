from solutions.ex3.distance import euclidean_distance

class Polygon(object):
    def __init__(self, vertices):
        self.vertices = vertices

    def get_perimeter(self):
        perimeter = 0
        for i in range(len(self.vertices)):
            v1 = self.vertices[i]
            v2 = self.vertices[(i + 1) % len(self.vertices)]
            perimeter += euclidean_distance(v1, v2)
        return perimeter

    def get_area(self):
        raise NotImplementedError()

if __name__ == '__main__':
    square = Polygon([(0,0), (1,0), (1,1), (0,1)])
    print square.get_perimeter()
from exercises.ex3.distance import euclidean_distance

class Polygon(object):
    def __init__(self, vertices):
        self.vertices = vertices

    # TODO: create a get_perimeter method here

    def get_area(self):
        raise NotImplementedError()

if __name__ == '__main__':
    square = Polygon([(0,0), (1,0), (1,1), (0,1)])
    print square.get_perimeter() # expected: 4.0
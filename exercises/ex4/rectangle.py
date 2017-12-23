from polygon import Polygon, euclidean_distance

class Rectangle(Polygon):
    def get_area(self):
        # TODO: add your code here
        pass

if __name__ == '__main__':
    r = Rectangle([(-1,-1), (1,-1), (1,1), (-1,1)])
    print r.get_perimeter() # expected: 8.0
    print r.get_area() # expected: 4.0
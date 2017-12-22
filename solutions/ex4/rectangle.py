from polygon import Polygon, euclidean_distance

class Rectangle(Polygon):
    def get_area(self):
        v0 = self.vertices[0]
        v1 = self.vertices[1]
        v2 = self.vertices[2]
        return euclidean_distance(v0, v1) * euclidean_distance(v1, v2)

if __name__ == '__main__':
    r = Rectangle([(-1,-1), (1,-1), (1,1), (-1,1)])
    print r.get_perimeter()
    print r.get_area()
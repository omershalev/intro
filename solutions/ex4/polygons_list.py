from solutions.ex4.polygon import Polygon
from solutions.ex4.rectangle import Rectangle
from solutions.ex4.triangle import Triangle

if __name__ == '__main__':
    polygons = [Triangle(vertices=[(0,0), (2,0), (1, 3)], base_length=2, height=3),
                Rectangle([(-1,-1), (1,-1), (1,1), (-1,1)]),
                Polygon([(0,-5), (1,-4), (0,-3), (-1,-3), (-2,-4), (-1,-5)])]
    for polygon in polygons:
        print 'For polygon with ' + str(len(polygon.vertices)) + ' vertices:'
        print 'Perimeter = ' + str(polygon.get_perimeter())
        try:
            print 'Area = ' + str(polygon.get_area())
        except NotImplementedError as e:
            print 'Cannot calculate area for a polygon of this degree'

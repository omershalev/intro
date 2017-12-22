import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

if __name__ == '__main__':
    p1 = (0,3)
    p2 = (4,0)
    print euclidean_distance(p1, p2)
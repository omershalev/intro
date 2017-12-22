from distance import euclidean_distance

if __name__ == '__main__':
    pairs_of_points = [((0,0), (0,1)),
                       ((0,0), (1,0)),
                       ((0,3), (4,0)),
                       ((0,0), (1,1))]
    distances = []
    for pair in pairs_of_points:
        distances.append(euclidean_distance(pair[0], pair[1]))
    print distances
    distances.sort()
    print 'min  = ', distances[0]
    print 'max = ', distances[-1]


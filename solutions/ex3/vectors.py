if __name__ == '__main__':
    points = {'A' : (0,0,0),
              'B' : (0,0,1),
              'C' : (0,1,0),
              'D' : (0,1,1),
              'E' : (1,0,0),
              'F' : (1,0,1),
              'G' : (1,1,0),
              'H' : (1,1,1)}
    vectors = {}

    for p1_name, p1_coordinates in points.items():
        for p2_name, p2_coordinates in points.items():
            if p1_name == p2_name:
                continue
            vectors[p1_name + p2_name] = (p2_coordinates[0] - p1_coordinates[0],
                                          p2_coordinates[1] - p1_coordinates[1],
                                          p2_coordinates[2] - p1_coordinates[2])
    print len(vectors)
    print vectors['AH']
    print vectors['HA']



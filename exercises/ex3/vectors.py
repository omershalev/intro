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

    # TODO: fill the dictionary with all 8*7 vectors

    print len(vectors) # expected: 56
    print vectors['AH'] # expected: (1, 1, 1)
    print vectors['HA'] # expected: (-1, -1, -1)



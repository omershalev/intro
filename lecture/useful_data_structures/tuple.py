if __name__ == '__main__':

    # Tuple definition
    t1 = (1, 2, 3)
    print t1
    t2 = (1, 'a', False, [1,2])
    print t2

    # Read a tuple element
    print t1[0]

    # Tuples are immutable
    t1[0] = 500 # this will raise an exception

    # Tuple length
    print len(t1)

    # The in operator
    print 2 in t1
    print 500 in t1

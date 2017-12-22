if __name__ == '__main__':

    # List definition
    l = [1,2,3,4,5,6]
    print l

    # Read a list element
    print l[0], l[5]
    # Negative indexing
    print l[-6], l[-1]

    # Modify a list element
    l[1] = 500
    print l

    # List slices
    print l[1:5]
    print l[1:5:2] # from:to:step

    # Append and remove list items
    l.append(7)
    print l
    l.pop()
    print l
    l.pop(0)
    print l

    # List concatenation
    l1 = [1,2]
    l2 = [3,4]
    print l1 + l2

    # List length
    print len(l)

    # The in operator
    print 3 in l
    print 400 in l

    # Various type elements
    l1 = ['a', 'b', 'c']
    print l1
    l2 = ['a', 2, False, [1, 2, 3]]
    print l2

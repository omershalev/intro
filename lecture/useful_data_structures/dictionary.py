if __name__ == '__main__':

    # Dictionary definition
    d = {'ONE' : 1, 'TWO' : 2, 'THREE' : 3}
    print d

    # Read a value from the dictionary
    print d['ONE']

    # Add a key-value pair to the dictionary
    d['FOUR'] = 4
    print d

    # Delete a key-value pair from the dictionary
    del d['ONE']
    print d

    # Access a key which doesn't exist in the dictionary
    # print d['FIVE'] # this will raise an exception

    # Check if a key exists in the dictionary
    print d.has_key('FIVE')
    print d.has_key('FOUR')
    print ('FOUR' in d) # the in operator also works

    # Get the list of keys
    print d.keys()

    # Get the list of values
    print d.values()

    # Get the list of pairs (tuples) key-value
    print d.items()

    # Ordered dict
    from collections import OrderedDict
    d = {'ONE' : 1, 'TWO' : 2, 'THREE' : 3}
    od = OrderedDict()
    od['ONE'] = 1
    od['TWO'] = 2
    od['THREE'] = 3
    print d
    print od # insertion order is preserved
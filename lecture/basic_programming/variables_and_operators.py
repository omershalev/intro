if __name__ == '__main__':

    # Integer definition
    x = 5
    print x
    print type(x)

    # Float definition
    x = 3.141592654
    print x
    print type(x)

    # String definition
    x = 'hello' # or "Hello"
    print x
    print type(x)

    # Boolean definition
    x = True # or False
    print x
    print type(x)

    # Simple operators
    x = 5
    y = 3
    print x + y
    print x - y
    print x * y
    print x / y # integer division

    x = 5.0
    print x / y # float division (if either x or y is float)
    print x // y # integer division

    print x % y # mod
    print x ** y # power

    # String concatenation
    x = 'Hello '
    y = 'World'
    print x + y

    print x * y # this will raise an exception

    # The not operator
    x = True
    print (not x)

    # Casting
    x = 5
    print str(x) + 'a'

    x = 1.0
    y = 0
    print bool(x)
    print bool(y)
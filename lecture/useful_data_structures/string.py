if __name__ == '__main__':

    # String definition
    s = 'hello world'
    print s

    # Read a single character
    print s[0]
    print s[-1]

    # Read substring
    print s[0:3]

    # Strings are immutable
    s[0] = 'a' # this will raise an exception

    # String length
    print len(s)

    # The in operator
    print ('hello' in s)

    # Capitalize
    print s.capitalize()

    # Uppercase
    print s.upper()

    # Lowercase
    print s.lower()

    # Split a string to a list of strings
    print s.split(' ') # whitespace is the delimiter

    # Join a list of strings to a single string
    print('**'.join(['life', 'is', 'so', 'beautiful']))
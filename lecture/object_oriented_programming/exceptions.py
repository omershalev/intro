if __name__ == '__main__':

    # Basic try-except-finally flow
    try:
        raise RuntimeError('hello')
        raise TypeError('world')
    except RuntimeError as e:
        print 'In RunTimeError handler'
        print e.message
    except TypeError as e:
        print 'In TypeError handler'
        print e.message
    finally:
        print 'In finally'

    # Define a custom exception
    class MySuperCoolException(Exception):
        pass

    # Raise a custom exception and catch it
    try:
        raise MySuperCoolException('This is super cool!!!')
    except MySuperCoolException as e:
        print e.message

    # Since inherited from Exception, this will also catch the custom exception
    try:
        raise MySuperCoolException('This is awesome!!!')
    except Exception as e:
        print e.message
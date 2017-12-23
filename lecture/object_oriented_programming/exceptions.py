'''
try:
    raise RuntimeError('hello')
    raise TypeError('world')
except RuntimeError as e:
    print 'In RunTimeError handler'
    print e.message
except TypeError as e:
    print 'In TypeError handler'
    print e.args
finally:
    print 'In finally'
'''
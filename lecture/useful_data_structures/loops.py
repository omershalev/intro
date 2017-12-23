import datetime
import time

if __name__ == '__main__':

    l = [1,2,3]
    t = (1,2,3)
    s = '123'
    d = {'ONE' : 1 ,'TWO' : 2, 'THREE' : 3}

    # Iterating over list elements
    for item in l:
        print item

    # Iterating over list indices and reading list elements accordingly
    for i in range(len(l)):
        print l[i]

    # Iterating over tuple elements
    for item in t:
        print item

    # Iterating over string characters
    for item in s:
        print item

    # Iterating over dictionary keys
    for key in d.keys(): # for key in d - also works
        print key

    # Iterating over dictionary values
    for value in d.values():
        print value

    # Iterating over dictionary key-value pairs
    for key, value in d.items():
        print str(key) + ' : ' + str(value)


    # While loop
    start_time = datetime.datetime.now()
    while datetime.datetime.now() - start_time < datetime.timedelta(seconds=5):
        print '*'
        time.sleep(1)

    # break and continue
    for i in range(100):
        if i % 2 == 0:
            continue
        if i > 20:
            break
        print i
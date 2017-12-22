from hour_getter import get_hour

def greet_me(name):
    hour = get_hour()
    if hour >= 6 and hour < 12:
        print 'Good morning, ' + name
    elif hour >= 12 and hour < 17:
        print 'Good afternoon, ' + name
    elif hour >= 17 and hour < 20:
        print 'Good evening, ' + name
    elif hour >= 20 and hour <= 23 or hour >= 0 and hour < 2:
        print 'Good night, ' + name
    else:
        print 'Go to sleep ' + name + '!'

if __name__ == '__main__':
    greet_me('Omer')
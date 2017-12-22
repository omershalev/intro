import datetime

def get_hour():
    now = datetime.datetime.now()
    hour = now.hour
    print 'The time now is ' + str(hour) + ' O\'clock'
    return hour

if __name__ == '__main__':
    get_hour()
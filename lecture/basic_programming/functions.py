def print_hello():
    print 'Hello World!'

def print_x(x):
    print x

def squared_x(x):
    return x**2

def give_me_five():
    return 5, 'five'

if __name__ == '__main__':

    x = 5

    print_hello()
    print_x(x)
    y = squared_x(5)
    print y
    five_int, five_string = give_me_five()
    print five_int, five_string
    five_tuple = give_me_five()
    print five_tuple
    print type(five_tuple)
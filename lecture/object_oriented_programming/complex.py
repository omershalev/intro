import math

class Complex(object):

    # Initializer
    def __init__(self, real, imaginary): # two arguments + self (as any other method)
        # Assign arguments into class members
        self.real = real
        self.imaginary = imaginary

    # Methods definition

    def show(self):
        print str(self.real) + ' + ' + str(self.imaginary) + 'i'  # access class members (self.real and self.imaginary)

    def modulus(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)



c1 = Complex(3,5) # implicitly calls __init__ with real=3 and imaginary=5
c1.show() # self is never explicitly mentioned in function calls
print c1.modulus()
print c1.real # access class member
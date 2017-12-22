class Animal(object):
    def __init__(self, weight, color, gender, age=None):
        self.weight = weight
        self.color = color
        self.gender = gender
        self.age = age

    def risk_for_human(self):
        if self.age is None:
            return self.weight ** 2
        return self.weight ** 2 - (self.age - 10)

    def is_attractive(self):
        if self.color in ['blue', 'red']:
            return True
        elif self.color == 'green' and self.gender == 'f':
            return True
        else:
            return False

    def update_weight(self, new_weight):
        self.weight = new_weight

if __name__ == '__main__':
    zoo = [Animal(200, 'pink', 'm', 8),
           Animal(60, 'green', 'f', 10),
           Animal(300, 'blue', 'm', 15),
           Animal(120, 'red', 'f', 13)]

    for animal in zoo:
        print 'risk_for_human is ' + str(animal.risk_for_human())

    print zoo[0].weight
    zoo[0].update_weight(500)
    print zoo[0].weight
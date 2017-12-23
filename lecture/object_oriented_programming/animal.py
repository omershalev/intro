class Animal(object):
    def __init__(self, name, weight, color, gender, age=None):
        self.name = name
        self.weight = weight
        self.color = color
        self.gender = gender
        self.age = age

    def risk_for_humans(self):
        if self.age is None:
            return self.weight ** 2
        return self.weight ** 2 - (self.age - 10)

    def is_attractive(self):
        raise NotImplementedError()

    def update_weight(self, new_weight):
        self.weight = new_weight

if __name__ == '__main__':
    friends = [Animal('Rachel', 200, 'pink', 'f', 8),
               Animal('Ross', 60, 'green', 'm', 10),
               Animal('Phoebe', 300, 'blue', 'f', 15),
               Animal('Chandler', 120, 'red', 'm', 13)]

    for animal in friends:
        print animal.name + '\'s risk level for humans is ' + str(animal.risk_for_humans())

    print 'Chandler\'s previous weight:'
    print friends[0].weight
    friends[0].update_weight(500)
    print 'Chandler\'s new weight:'
    print friends[0].weight
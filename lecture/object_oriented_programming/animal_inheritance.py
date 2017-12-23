from animal import Animal

class Elephant(Animal):
    def __init__(self, name, weight, color, gender, age=None, trunk_length=None):
        super(Elephant, self).__init__(name, weight, color, gender, age)
        self.trunk_length = trunk_length

    def is_attractive(self):
        if self.trunk_length > 7:
            return True
        return False

class Lion(Animal):
    def __init__(self, name, weight, color, gender, age=None):
        super(Lion, self).__init__(name, weight, color, gender, age)

    def is_attractive(self):
        if self.weight > 200:
            return True
        return False

    def is_stronger_than(self, other):
        if self.weight > other.weight and self.age > other.age:
            return True
        return False

if __name__ == '__main__':
    elephant_1 = Elephant(name='Babar', weight=400, color='gray', gender='m', age=15, trunk_length=9.5)
    lion_1 = Lion(name='Simba', weight=120, color='brown', gender='m', age=2)
    lion_2 = Lion(name='Mufasa', weight=220, color='brown', gender='m', age=5)

    map_bool_to_prints = {True : ' is ', False : ' is not '}

    print lion_2.name + map_bool_to_prints[lion_2.is_stronger_than(lion_1)] + 'stronger than ' + lion_1.name
    print lion_1.name + map_bool_to_prints[lion_1.is_stronger_than(lion_2)] + 'stronger than ' + lion_2.name

    elephants_and_lions = [elephant_1, lion_1, lion_2]
    for animal in elephants_and_lions:
        print animal.name + map_bool_to_prints[animal.is_attractive()] + 'attractive'

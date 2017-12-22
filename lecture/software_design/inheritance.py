from classes import Animal

class Elephant(Animal):
    def __init__(self, weight, color, gender, age=None, trunk_length=None):
        super(Elephant, self).__init__(weight, color, gender, age)
        self.trunk_length = trunk_length

    def is_attractive(self):
        if self.trunk_length > 7:
            return True
        return False

class Lion(Animal):
    def __init__(self, weight, color, gender, age=None):
        super(Lion, self).__init__(weight, color, gender, age)

    def is_stronger_than(self, other):
        if self.weight > other.weight and self.age > other.age:
            return True
        return False

if __name__ == '__main__':
    elephant_1 = Elephant(weight=400, color='gray', gender='f', age=15, trunk_length=9.5)
    print elephant_1.is_attractive()

    lion_1 = Lion(weight=120, color='brown', gender='m', age=2)
    lion_2 = Lion(weight=220, color='brown', gender='f', age=5)
    print lion_2.is_stronger_than(lion_1)

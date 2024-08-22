class PartyAnimal:

    # Constructor. Which is typically used to set up variables
    def __init__(self):
        self.x = 0
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print("So Far", self.x)

    # destructor. This is hardly ever used
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an = 42
print('an contains', an)
print('')


class Person:

    def __init__(self, z, a):
        self.x = 0
        self.name = z
        self.age = a
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def show_age(self):
        print(self.name, "is", self.age, "years old")

s = Person("Sally", 33)
s.party()
j = Person("Jim", 45)

j.party()
s.party()

s.show_age()
j.show_age()
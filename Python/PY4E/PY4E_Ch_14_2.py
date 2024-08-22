class PartyAnimal:

    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So Far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

class Dog:
    def __init__(self, name):
        self.tb = 0
        self.name = name  # Set the dog's name based on user input

    def bark(self, times=1):
        for _ in range(times):
            self.tb += 1
            print('bark')

    def times(self):
        print(self.name, 'has barked', self.tb, 'times')

# Prompt the user for the dog's name
dog_name = input("Enter the dog's name: ").capitalize() # Forcing capitalization on the name

# Create a new Dog instance with that name
my_dog = Dog(dog_name)

# Prompt the user for the number of times the dog should bark
try:
    # By default input is a string. So convert it to an int
    barks = int(input(f"How many times does {dog_name} bark? "))
    my_dog.bark(barks)
except ValueError:
    print("Invalid number.", dog_name, "didn't bark")

# Print how many times the dog barked
my_dog.times()

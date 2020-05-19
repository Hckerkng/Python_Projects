# Demonstrate classes and inheritance with the Animal class and subclasses.
# TPRG 2131 Fall 2019
# Louis Bertrand
# 2019-09-17 Initial version

class Animal(object):
    """Model the behaviour of a generic animal."""
    def __init__(self, name):
        self.name = name
        self.is_sleeping = False

    def draw_picture(self):
        return "<no picture>"

    @property
    def sound(self):
        return "grunt"

    @property
    def sleep(self):
        return self.is_sleeping

    @sleep.setter
    def sleep(self, status):
        self.is_sleeping = status


class Dog(Animal):
    """Model the behaviour of a dog."""
    def __init__(self, name):
        super().__init__(name)

    @property
    def sound(self):
        return "woof"

    def __str__(self):
        return "Dog named " + self.name


if __name__ == "__main__":
    # testing the classes

    critter = Animal("Fluffy")
    print(critter)
    print(critter.sleep)
    critter.sleep = True
    print(critter.sleep)

    ruff = Dog("Ruff")
    print(ruff)

    # Showing the override of the sound property
    print(ruff.sound)
    print(critter.sound)

    
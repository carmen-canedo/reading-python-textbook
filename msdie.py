# msdie.py
#   Class definition for an n-sided die

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


def main():

    die1 = MSDie(8)

    print(die1.get_value())

if __name__ == '__main__':
    main()

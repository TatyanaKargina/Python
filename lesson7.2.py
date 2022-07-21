from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.parameter)


class Coat(Clothes):

    @property
    def expense(self):
        return self.parameter / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.parameter * 2 + 0.3


coat = Coat(50)
suit = Suit(1.80)

print(coat.expense)
print(suit.expense)
print(coat.expense + suit.expense)
from abc import ABC, abstractmethod

class Defolt_class(ABC):

    @abstractmethod
    def defolt_method(self):
        pass

class Clothes(Defolt_class):

    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def square_jacket(self):
        s_jack = self.growth * 2 + 0.3
        return s_jack

    def square_coat(self):
        s_coat = self.size / 6.5 + 0.5
        return s_coat

    @property
    def total_consumpt(self):
        return (self.growth * 2 + 0.3) + (self.size / 6.5 + 0.5)

    def defolt_method(self):
        pass

class Coat(Clothes):
    pass

class Jacket(Clothes):
    pass


coat = Coat(21, 13)
jacket = Jacket(21,13)

print(f' площадь ткани для костюма {jacket.square_jacket()}')
print(f' площадь ткани для пальто {coat.square_coat()}')
print(f'общий объем ткани {jacket.total_consumpt}')


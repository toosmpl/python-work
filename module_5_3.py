class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(self, new_flour):
        for i in range(1, new_flour + 1):
            if new_flour > self.number_of_flours or new_flour < 1:
                print("Такого этажа не существует:)")
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_flours

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.__len__()}")


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_flours == other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_flours < other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_flours <= other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_flours > other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_flours >= other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_flours != other.number_of_flours
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, value):
        self.number_of_flours += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

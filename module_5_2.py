class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(self, new_flour):
        for i in range(1, new_flour + 1):
            if new_flour > self.number_of_flours or new_flour < 1:
                print("Такого этажа не существует and you are gay :)")
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_flours

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.__len__()}")


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

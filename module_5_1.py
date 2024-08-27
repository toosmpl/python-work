class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(self, new_flour):
        for i in range(1, new_flour+1):
            if new_flour > self.number_of_flours or new_flour < 1:
                print("Такого этажа не существует and you are gay :)")
                break
            else:
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


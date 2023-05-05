
class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.residents = []

    def add_persons(self, person):
        self.residents.append(person)

    def remove_persons(self, person):
        self.residents.remove(person)

    def print_persons(self):
        print(self.address)
        for resident in self.residents:
            print(resident.name,resident.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("umar", 23)
p2 = Person("ubaid", 21)
p3 = Person("wahib", 23)


house = House("Name of the house is: " "House of the Lords",7)
house.add_persons(p1)
house.add_persons(p2)
house.add_persons(p3)


house.print_persons()  

house.remove_persons(p3)
house.print_persons()  


    

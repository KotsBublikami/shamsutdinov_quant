class Animal:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def make_sound(self):
        print("I AM IRON MAN")



animal = Animal('blue', "Ozzy")
animal.make_sound()


class Dog(Animal):
    def __init__(self, color, name, master):
        Animal.__init__(self, color, name)
        self.master = master
    def make_sound(self):
        print("wafwaf")

dog = Dog('red', 'Oxygen', 'wolf')
dog.make_sound()


class Cat(Animal):
    def __init__(self, color, name, hvost):
        Animal.__init__(self, color, name)
        self.hvost = hvost
    def make_sound(self):
        print("meyoooow")

cat = Cat('turtle', 'gay', "3 метра")
cat.make_sound()




class DnD_Character:
    def __init__(self, name, rasa, height):
        self.name = name
        self.rasa = rasa
        self.height = height

class Elf(DnD_Character):
    def __init__(self, name, rasa, height):
        super().__init__( name, rasa, height)
    def class_ckills(self):
        print("дальнобойное оружие для геев")

elf = Elf('gay ', 'elf','2 meters')
elf.class_ckills()

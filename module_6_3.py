import random


class Animal:
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа

    def __init__(self, speed):
        self.speed = speed #скорость передвижения существа (определяется при создании объекта)
        self._cords = [0, 0, 0] #координаты в пространстве.

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal): # Класс описывающий птиц.
    beak = True # наличие клюва

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal): # Класс описывающий плавающего животного.
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(abs((dz) * self.speed / 2))


class PoisonousAnimal(Animal):  #Класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()


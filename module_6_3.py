class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]
        
    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')




class Bird(Animal):
    pass


class AquaticAnimal(Animal):
    pass

class PoisonousAnimal(Animal):
    pass


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"



db = Duckbill(10)
print(db.live)

# print(db.beak)
# db.speak()
# db.attack()
db.move(1, 2, 3)
db.get_cords()
# db.dive_in(6)
# db.get_cords()
# db.lay_eggs()


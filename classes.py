class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет меня зовут {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в {self.group}')


class Students(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()








# human = Human('Well')
# print(human.name)
student = Students('Ivan', 'Urban', 'Pythton 1')
# student.about()
print(StudentGroup.mro())
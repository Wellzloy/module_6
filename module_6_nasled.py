class Human:
    head = True

    def say_hello(self):
        print('Здравствуйте')





class Student(Human):
    head = False
    def about(self):
        print('Я студент')

class Teacher(Human):
    pass




# human = Human()
stugent = Student()
teacher = Teacher()
stugent.say_hello()
teacher.say_hello()
print(teacher.head)
print(stugent.head)

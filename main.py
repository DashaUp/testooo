
class Student:
    amount_of_students = 0

    def __init__(self, name, age, height = 160):
        self.age = age
        self.height = height
        Student.amount_of_students += 1
        self.name = name

    def happy_birthday(self):
        print(f'Greetings! {self.name} you have HB')
        self.age +=1

    def __str__(self):
        return f'<Student name ={self.name} age = {self.age} height={self.height}>'


s1 = Student(28, 180)
s1.happy_birthday()
print('Alex', s1.age, s1.height)

s2 = Student(18, 50)
print('Bob', s2.age, s2.height)

s3 = Student(17, 150)
print('Jane', s3.age, s3.height)

print("Amount", Student.amount_of_students)

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
            return 3.14 * (self.radius ** 2)

circle_10 = Circle(10)
print(circle_10.calc_area())

circle_3 = Circle(3)
print(circle_3.calc_area())


import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('time to study')
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('time to sleep')
        self.gladness +=3

    def to_chill(self):
        print('time to chill')
        self.gladness += 5
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < - 0.5:
            print('Too lazy...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False
        elif self.progress > 5:
            print('Genius! passed!')
            self.alive = False

    def end_of_day(self):
        print(
            f"gladness - {self.gladness}\n"
            f"progress - {round(self.progress, 2)}"
        )

    def live(self, day):
        print(
            f"Day#{day} of {self.name} life"
        )
        magic = random.randint(1, 3)
        if magic == 1:
            self.to_study()
        elif magic == 2:
            self.to_sleep()
        elif magic == 3:
            self.to_chill()

            self.end_of_day()
            self.is_alive()


bob = Student('Bob')
for day in range(1, 365):
    if bob.alive() == False:
        break
    bob.live(day)

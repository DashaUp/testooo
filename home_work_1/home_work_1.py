class MyVirtualEnvironment:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, my dear teacher. I am new environment: " + self.name)


myVirtualEnvironment = MyVirtualEnvironment("environment".upper())
myVirtualEnvironment.say_hi()

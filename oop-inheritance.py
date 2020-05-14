# parent
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoIsThis()
peggy.swim() # accessing method from parent class.
peggy.run() # penguins own new method.

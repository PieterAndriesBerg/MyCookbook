class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000 # we cant change it here because python treats the __maxprice as private attributes. We must use the setter method to change this attribute.
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

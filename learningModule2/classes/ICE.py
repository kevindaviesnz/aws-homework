from .Car import Car

class ICE(Car):
    def __init__(self, brand, range):
        super().__init__(brand)
        self.range = range
    def drive(self):
        print("Driving my petrol car")

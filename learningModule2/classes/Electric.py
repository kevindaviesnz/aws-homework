from .Car import Car

class Electric(Car):
    def __init__(self, brand, range):
        super().__init__(brand)
        self.range = range
    def drive(self):
        print("Driving")

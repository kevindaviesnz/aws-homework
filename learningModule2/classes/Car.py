
class Car:
    
    def __init__(self, brand):
        self.brand = brand
        self.milage_km = 0
    
    def drive(self, distance_km):
        self.milage_km += distance_km